# AI-Powered Network Configuration Auditor

Audits Ericsson 4G/5G network configuration exports, flags misconfigured
parameters, and explains each finding against the vendor documentation —
with a language model that runs entirely on-premise.

Built during an internship at **inwi** (telecom operator, Casablanca).
Network configuration data could not leave the operator's infrastructure,
so every component, including the LLM, runs locally.

---

## The problem

A single Bulk CM export describes thousands of network objects, each with
hundreds of parameters. Engineers reviewed them by hand. The errors that
mattered — a neighbour relation with an inconsistent offset, a parameter
drifting from the reference value — were the ones nobody noticed.

## What it does

The pipeline has three layers, each usable on its own.

**1. Parsing** — `src/parser.py`
Reads Ericsson Bulk CM XML (3GPP format) with lxml and flattens it into
one CSV table per object type: cells, neighbour relations (4G/3G/2G),
and the rest.

**2. Detection** — `src/detection_ml.py` and `src/conformite.py`
Two complementary passes:
- *Statistical*: unsupervised outlier detection across neighbour
  relations, which surfaces values that are inconsistent with their
  peers rather than merely out of range.
- *Conformance*: rule-based checks of critical parameters against
  reference values.

**3. Explanation** — `src/rag_explain.py` and `src/rag_index.py`
A retrieval-augmented pipeline turns each finding into a technical
explanation grounded in Ericsson documentation:
- Verified parameter sheets, retrieved by exact name, are the priority
  source.
- PDF documentation chunks, retrieved semantically from ChromaDB,
  complete the context.
- The model answers only from retrieved material.

Every explanation records whether a verified sheet backed it
(`source_fiche`), so an engineer can tell a documented answer from an
inferred one.

### Never guess

This is the constraint the whole design is built around. A small local
model asked about a network parameter will produce something fluent and
wrong unless it is stopped. The prompt makes refusal the required
behaviour:

> If nothing describes the parameter, answer exactly:
> "The indexed documentation contains no usable information on this
> parameter." Invent nothing.

Generation runs at `temperature=0.1`. A confident wrong answer is worse
than no answer, because the engineer stops checking.

## Architecture

```
Bulk CM XML
    │
    ├─ parser.py ─────────► CSV tables (one per object type)
    │
    ├─ detection_ml.py ───► statistical anomalies
    ├─ conformite.py ─────► conformance violations
    │
    └─ rag_explain.py ────► grounded explanations
            ▲
            │  verified sheets (exact match) + PDF chunks (ChromaDB)
            │
       rag_index.py ──────► builds the shared vector index
```

`pipeline.py` orchestrates the four stages. `api.py` exposes them over
HTTP.

## API

FastAPI backend with background processing — an audit runs for minutes,
so the upload returns immediately with a job id.

| Method | Endpoint                  | Purpose                          |
|--------|---------------------------|----------------------------------|
| POST   | `/audit`                  | Upload an XML, returns `job_id`  |
| GET    | `/audit/{job_id}/status`  | Processing status                |
| GET    | `/audit/{job_id}/report`  | Full JSON report once complete   |
| GET    | `/health`                 | API and Ollama reachability      |

Each audit gets an isolated working directory, so several can run
concurrently. The ChromaDB index is shared and built once. If Ollama is
unavailable, detection still returns results and the report carries an
explicit `rag_erreur` field rather than failing.

## Stack

| Layer      | Technology                                      |
|------------|-------------------------------------------------|
| Parsing    | lxml, pandas                                    |
| Detection  | scikit-learn                                    |
| Retrieval  | ChromaDB, `nomic-embed-text`                    |
| Generation | Ollama, Llama 3.2 — fully local                 |
| API        | FastAPI, Uvicorn                                |
| Frontend   | HTML/JS single page                             |
| Tooling    | uv, Python ≥ 3.10                               |

## Running it

```bash
# install dependencies
uv sync

# pull the local models
ollama pull llama3.2
ollama pull nomic-embed-text

# build the documentation index (once)
uv run python src/rag_index.py

# full pipeline on a file
uv run python main.py

# or serve the API
uv run uvicorn src.api:app --reload --port 8000
```

`data/` contains a sample Bulk CM export. `docs/` holds the Ericsson
reference material the index is built from. Sample outputs are in
`outputs/`.

## Design decisions

**A local model, by constraint.** No API was permitted. That ruled out
compensating for weak retrieval with a stronger model, so most of the
work went into the retrieval layer: how the documentation is chunked,
what gets embedded, and which source wins when two disagree.

**Two retrieval paths, not one.** Exact-name lookup on verified parameter
sheets is more reliable than semantic search for this task. Semantic
search over the PDFs fills the gaps. The prompt states which source takes
priority.

**Detection separated from explanation.** The statistical and conformance
layers produce findings without any model involvement. The LLM only
explains. A failure in the explanation layer never invents a finding.

---

**Ilias EL AMRANI** · [LinkedIn](https://linkedin.com/in/iliaselamrani)
