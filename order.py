import json

with open('sbm_extracted_text.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Sort by numeric page number, then rekey to sequential integers
sorted_keys = sorted(data.keys(), key=lambda k: int(k.split('_')[1]))
ordered = {str(i): data[k] for i, k in enumerate(sorted_keys, start=1)}

with open('sbm_ordered.json', 'w', encoding='utf-8') as f:
    json.dump(ordered, f, ensure_ascii=False, indent=2)

print(f"Done. {len(ordered)} pages reordered.")
for i, orig_key in enumerate(sorted_keys, start=1):
    print(f"  {i} <- {orig_key}")
