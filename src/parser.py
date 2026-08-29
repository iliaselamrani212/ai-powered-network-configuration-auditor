from pathlib import Path
import pandas as pd
from lxml import etree

NS = {
    "xn": "genericNrm.xsd",
    "es": "EricssonSpecificAttributes.16.28.xsd",
    "un": "utranNrm.xsd",
    "gn": "geranNrm.xsd",
}

BASE_DIR = Path(__file__).resolve().parent.parent
XML_PATH = BASE_DIR / "data" / "cm_exp_20181012_162725.xml"
OUT_DIR = BASE_DIR / "outputs" / "tables"


def local_name(tag: str) -> str:
    return etree.QName(tag).localname


def extract_params(vsdata_element) -> dict:
    params = {}

    def walk(el, prefix=""):
        for child in el:
            name = local_name(child.tag)
            key = f"{prefix}{name}"
            if len(child) > 0:
                walk(child, prefix=f"{key}.")
            else:
                params[key] = (child.text or "").strip()

    walk(vsdata_element)
    return params


def parse(xml_path: Path) -> dict:
    tree = etree.parse(str(xml_path))
    root = tree.getroot()

    objets = {}

    def descendre(element, chemin_parent):
        for enfant in element:
            nom = local_name(enfant.tag)

            if nom in ("SubNetwork", "MeContext", "ManagedElement"):
                seg = f"{nom}={enfant.get('id')}"
                descendre(enfant, chemin_parent + [seg])

            elif nom == "VsDataContainer":
                cid = enfant.get("id")

                vtype_el = enfant.find("xn:attributes/xn:vsDataType", NS)
                if vtype_el is None:
                    descendre(enfant, chemin_parent)
                    continue

                vtype = vtype_el.text.strip()
                seg = f"{vtype}={cid}"
                dn = ",".join(chemin_parent + [seg])

                vsdata_el = enfant.find(f"xn:attributes/es:{vtype}", NS)
                ligne = {"DN": dn, "id": cid, "vsDataType": vtype}
                if vsdata_el is not None:
                    ligne.update(extract_params(vsdata_el))

                objets.setdefault(vtype, []).append(ligne)

                descendre(enfant, chemin_parent + [seg])

            else:
                descendre(enfant, chemin_parent)

    descendre(root, [])
    return objets


def exporter(objets: dict, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for vtype, lignes in objets.items():
        df = pd.DataFrame(lignes)
        cols = ["DN"] + [c for c in df.columns if c != "DN"]
        df = df[cols]
        df.to_csv(out_dir / f"{vtype}.csv", index=False, encoding="utf-8")


def main():
    print(f"Lecture de : {XML_PATH}")
    objets = parse(XML_PATH)

    total = sum(len(v) for v in objets.values())
    print(f"\n{total} objets extraits, {len(objets)} types distincts.\n")

    controle = {
        "vsDataUtranCellRelation": 74,
        "vsDataGeranCellRelation": 55,
        "vsDataEUtranCellRelation": 38,
        "vsDataEUtranCellFDD": 3,
    }
    print("Verification des comptages cles :")
    for vtype, attendu in controle.items():
        trouve = len(objets.get(vtype, []))
        etat = "OK" if trouve == attendu else "!! ECART"
        print(f"  {vtype:<28} attendu {attendu:>3} | trouve {trouve:>3}  {etat}")

    exporter(objets, OUT_DIR)
    print(f"\nCSV ecrits dans : {OUT_DIR}")


if __name__ == "__main__":
    main()