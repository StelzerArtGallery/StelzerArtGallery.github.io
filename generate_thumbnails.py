import os
import json
from pathlib import Path
from PIL import Image

# Configuration
THUMBNAIL_SIZE = (435, 350)  # width, height
THUMBNAIL_SUFFIX = '-thumb'

def generate_thumbnails():
    # Load categories
    with open('assets/categories.json', 'r', encoding='utf-8') as f:
        categories = json.load(f)

    for category in categories:
        folder_path = Path(category['folder'])
        thumbnails_folder = folder_path / 'thumbnails'
        thumbnails_folder.mkdir(exist_ok=True)

        thumbnails = []
        for img_name in category['images']:
            img_path = folder_path / img_name
            if not img_path.exists():
                continue

            # Generate thumbnail filename
            name_parts = img_name.rsplit('.', 1)
            thumb_name = f"{name_parts[0]}{THUMBNAIL_SUFFIX}.{name_parts[1]}"
            thumb_path = thumbnails_folder / thumb_name

            # Skip if thumbnail already exists
            if thumb_path.exists():
                print(f"Thumbnail already exists: {thumb_path}")
                thumbnails.append(thumb_name)
                continue

            try:
                # Open image and create thumbnail
                with Image.open(img_path) as img:
                    img.thumbnail(THUMBNAIL_SIZE)
                    # Save with same format
                    img.save(thumb_path, img.format)
                    print(f"Generated thumbnail: {thumb_path}")
                    thumbnails.append(thumb_name)
            except Exception as e:
                print(f"Error processing {img_path}: {e}")

        # Update category with thumbnails
        category['thumbnails'] = thumbnails

    # Save updated categories.json
    with open('assets/categories.json', 'w', encoding='utf-8') as f:
        json.dump(categories, f, indent=2)

if __name__ == '__main__':
    generate_thumbnails()