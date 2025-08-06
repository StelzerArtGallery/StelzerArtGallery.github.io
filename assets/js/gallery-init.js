// This script loads categories and images from categories.json and injects them into the homepage.
fetch('/assets/categories.json')
  .then(res => res.json())
  .then(categories => {
    window.categories = categories;
    if (typeof renderCategoryGrid === 'function') renderCategoryGrid();
    if (typeof startFadeGallery === 'function') startFadeGallery();
  });
