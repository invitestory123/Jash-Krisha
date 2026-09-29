# scratch/verify_all.py
import re

files_to_check = [
    'index.html',
    'editable/wedding-data.js',
    'assets/custom.css'
]

unwanted_strings = [
    'Debanu', 'Diya Saha', 'Agartala', 'Tripura', 'Swarnabhumi', 'Malancha', 'Manikya',
    'Chirag', 'Het', 'Navrangpura', 'Ahmedabad', 'The Grand Bhavan'
]

for fp in files_to_check:
    with open(fp, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f'Checking {fp}...')
    for s in unwanted_strings:
        if s.lower() in text.lower():
            print(f'  WARNING: Found unwanted string "{s}" in {fp}')

# Also check bundle JS for specific old names
with open('assets/index-2d1L6cXj.js', 'r', encoding='utf-8') as f:
    bundle_text = f.read()

for s in ['Debanu', 'Diya Saha', 'Swarnabhumi', 'Malancha']:
    if s.lower() in bundle_text.lower():
        print(f'  WARNING: Found unwanted string "{s}" in bundle JS!')

print("Verification complete!")
