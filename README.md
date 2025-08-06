# Stelzer Art Gallery

A modern, beautiful, and user-friendly art gallery website built with Jekyll and GitHub Pages.

## Features
- Dark gray gradient background with white text (except navigation)
- Responsive grid layout for images and categories
- Landing page with category thumbnails and labels
- Each category links to its own gallery page
- Fade gallery on home page, fading between images at random intervals (20-40s)
- Automated gallery page creation for each category (folder)
- Easy to update: just import your images into folders and run the script

## Setup
1. Place your images in subfolders under the root (e.g., `landscapes/`, `portraits/`, etc.).
2. Run the provided Python script to generate category data and gallery pages.
3. Update the `categories` array in `index.html` with your categories and images (or automate this step).
4. Deploy to GitHub Pages.

## Customization
- Edit `_layouts/default.html` and `assets/css/style.css` for layout and style changes.
- Update navigation in `_layouts/default.html` as needed.

## License
Free for personal and non-commercial use.
