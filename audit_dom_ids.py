import re
import sys

# Safe UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open('BL400K.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all document.getElementById('...') in script
script_start = text.find('<script>')
script_text = text[script_start:]

ids_in_script = set(re.findall(r"document\.getElementById\(['\"]([^'\"]+)['\"]\)", script_text))
print(f"Total unique IDs referenced in script: {len(ids_in_script)}")

# Check each ID against the HTML
missing_ids = []
for el_id in sorted(ids_in_script):
    pattern = rf'id=["\']{re.escape(el_id)}["\']'
    found = re.search(pattern, text)
    status = "OK" if found else "MISSING"
    if not found:
        missing_ids.append(el_id)
    print(f"  [{status}] {el_id}")

print("\n--- SUMMARY OF MISSING IDS ---")
if missing_ids:
    for m in missing_ids:
        print(f"[ERROR] MISSING IN DOM: {m}")
    sys.exit(1)
else:
    print("[SUCCESS] All IDs referenced in script exist in DOM 100%!")
    sys.exit(0)
