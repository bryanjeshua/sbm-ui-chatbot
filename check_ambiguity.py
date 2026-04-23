import json
from collections import defaultdict

with open('browse_data.json', encoding='utf-8') as f:
    d = json.load(f)

structural = {"items","per_kota","per_provinsi","per_provinsi_kategori",
              "per_negara_kategori","sewa_insidentil_per_provinsi"}

def crumb(path):
    parts = path.split(" > ")
    if len(parts) <= 2: return ""
    middle = [p for p in parts[1:-1] if p not in structural]
    if not middle: return ""
    return " > ".join(p.replace("_"," ") for p in middle)

for lamp_key, lamp_info in d.items():
    groups = defaultdict(list)
    for r in lamp_info["rows"]:
        u = (r.get("uraian") or "").strip()
        if u:
            groups[u].append(r)

    for u, rows in groups.items():
        if len(rows) < 2: continue
        besarans = set(r["besaran"] for r in rows)
        if len(besarans) < 2: continue

        crumbs = [crumb(r["path"]) for r in rows]
        unique_crumbs = set(crumbs)
        still_bad = len(unique_crumbs) < len(rows) or "" in unique_crumbs

        tag = "AMBIGUOUS" if still_bad else "ok"
        print(f"\n[{tag}] Lamp {lamp_key} | {repr(u)}")
        for r, c in zip(rows, crumbs):
            print(f"  [{c or '(NO CRUMB)':<45}] {r['besaran']}")
