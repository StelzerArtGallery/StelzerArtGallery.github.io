import glob
import re

# List all gallery HTML files (adjust the pattern if needed)
gallery_files = glob.glob("*.html")

for filename in gallery_files:
    # Skip non-gallery files if needed
    if filename.lower() in ["index.html", "404.html"]:
        continue
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    # Add loading="lazy" to <img> tags that don't already have it
    new_content = re.sub(
        r'(<img\s[^>]*)(?<!loading="lazy")>',
        lambda m: m.group(1).rstrip() + ' loading="lazy">',
        content
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated {filename}")

print("Bulk update complete!")