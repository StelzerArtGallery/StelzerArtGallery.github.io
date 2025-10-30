import os
import json
from pathlib import Path


# Configuration
GALLERY_ROOT = Path('assets/images')
CATEGORIES = []

# Mapping of folder names to display names
DISPLAY_NAMES = {
    'Autumn': 'Autumn',
    'Barns': 'Barns',
    'Birds': 'Birds',
    'Bluebonnets': 'Bluebonnets',
    'CrashingWaves': 'Crashing Waves',
    'Floral': 'Floral',
    'JustTrees': 'Just Trees',
    'Lighthouses': 'Lighthouses',
    'OldOaks': 'Old Oaks',
    'SandDunes': 'Sand Dunes',
    'Seashells': 'Seashells',
    'StillLife': 'Still Life',
    'Stumps': 'Stumps',
    'Water&Trees': 'Water & Trees',
    'Waterfalls': 'Waterfalls',
    'Winter': 'Winter',
}

# Find all category folders inside assets/images
if GALLERY_ROOT.exists():
    for folder in GALLERY_ROOT.iterdir():
        if folder.is_dir():
            images = [f.name for f in folder.iterdir() if f.suffix.lower() in {'.jpg', '.jpeg', '.png', '.gif', '.webp'}]
            if images:
                display_name = DISPLAY_NAMES.get(folder.name, folder.name.replace('-', ' ').title())
                CATEGORIES.append({
                    'name': display_name,
                    'folder': f'assets/images/{folder.name}',
                    'images': images
                })

# Write categories.json for use in index.html
with open('assets/categories.json', 'w', encoding='utf-8') as f:
    json.dump(CATEGORIES, f, indent=2)

# Generate a gallery page for each category

# Prepare navigation for categories (alphabetical order)
cat_names = [cat['name'] for cat in CATEGORIES]
cat_files = [f"{cat['folder'].split('/')[-1]}.html" for cat in CATEGORIES]

GALLERY_LAYOUT = '''---
layout: default
title: {cat_name}
---
<div class="category-nav" style="display:flex;justify-content:space-between;align-items:center;margin-bottom:2rem;">
  <a href="{prev_file}" class="cat-nav-arrow" title="Previous: {prev_name}" style="font-size:2rem;text-decoration:none;">&#8592;</a>
  <span style="font-size:1.3rem;font-weight:500;">{cat_name}</span>
  <a href="{next_file}" class="cat-nav-arrow" title="Next: {next_name}" style="font-size:2rem;text-decoration:none;">&#8594;</a>
</div>
<div class="gallery-grid">
  {images}
</div>
<div class="category-nav" style="display:flex;justify-content:space-between;align-items:center;margin-top:2rem;">
  <a href="{prev_file}" class="cat-nav-arrow" title="Previous: {prev_name}" style="font-size:2rem;text-decoration:none;">&#8592;</a>
  <span style="font-size:1.3rem;font-weight:500;">{cat_name}</span>
  <a href="{next_file}" class="cat-nav-arrow" title="Next: {next_name}" style="font-size:2rem;text-decoration:none;">&#8594;</a>
</div>
'''


for idx, cat in enumerate(CATEGORIES):
    img_tags = '\n  '.join([
        f'<a class="gallery-item" href="/{cat['folder']}/{img}" target="_blank">'
        f'<img src="/{cat['folder']}/{img}" alt="{cat['name']} artwork" loading="lazy">'
        '</a>' for img in cat['images']
    ])
    prev_idx = (idx - 1) % len(CATEGORIES)
    next_idx = (idx + 1) % len(CATEGORIES)
    page_content = GALLERY_LAYOUT.format(
        cat_name=cat['name'],
        images=img_tags,
        prev_file=cat_files[prev_idx],
        next_file=cat_files[next_idx],
        prev_name=cat_names[prev_idx],
        next_name=cat_names[next_idx]
    )
    html_filename = f"{cat['folder'].split('/')[-1]}.html"
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(page_content)

print('Gallery pages and categories.json generated.')
