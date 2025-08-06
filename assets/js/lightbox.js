// Lightbox for category gallery pages
(function() {
  if (!document.querySelector('.gallery-grid')) return;
  // Create lightbox elements
  const lightbox = document.createElement('div');
  lightbox.id = 'lightbox-overlay';
  lightbox.innerHTML = `
    <div class="lightbox-backdrop"></div>
    <div class="lightbox-content">
      <button class="lightbox-close" aria-label="Close">&times;</button>
      <button class="lightbox-arrow left" aria-label="Previous">&#8592;</button>
      <img class="lightbox-img" src="" alt="Artwork">
      <button class="lightbox-arrow right" aria-label="Next">&#8594;</button>
    </div>
  `;
  document.body.appendChild(lightbox);
  const overlay = document.getElementById('lightbox-overlay');
  const img = overlay.querySelector('.lightbox-img');
  const closeBtn = overlay.querySelector('.lightbox-close');
  const leftBtn = overlay.querySelector('.lightbox-arrow.left');
  const rightBtn = overlay.querySelector('.lightbox-arrow.right');
  const backdrop = overlay.querySelector('.lightbox-backdrop');
  let images = Array.from(document.querySelectorAll('.gallery-item img'));
  let current = 0;
  function show(idx) {
    if (idx < 0) idx = images.length - 1;
    if (idx >= images.length) idx = 0;
    current = idx;
    img.src = images[current].src;
    img.alt = images[current].alt;
    // Set tooltip (title) to file name
    const src = images[current].src || images[current].getAttribute('src');
    let fileName = src.split('/').pop();
    img.title = fileName;
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
  function hide() {
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }
  images.forEach((el, i) => {
    el.parentElement.addEventListener('click', e => {
      e.preventDefault();
      show(i);
    });
  });
  closeBtn.onclick = hide;
  backdrop.onclick = hide;
  leftBtn.onclick = () => show(current - 1);
  rightBtn.onclick = () => show(current + 1);
  document.addEventListener('keydown', e => {
    if (!overlay.classList.contains('active')) return;
    if (e.key === 'Escape') hide();
    if (e.key === 'ArrowLeft') show(current - 1);
    if (e.key === 'ArrowRight') show(current + 1);
  });
})();
