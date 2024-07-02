// JavaScript for Lightbox Functionality
let currentImageIndex = 0;
const images = document.querySelectorAll('.gallery-imgss');
const lightbox = document.getElementById('lightboxss');
const lightboxImg = document.getElementById('lightbox-img');
const lightboxControls = document.querySelector('.lightbox-controls');
const prevArrow = lightboxControls.querySelector('.prev');
const nextArrow = lightboxControls.querySelector('.next');

images.forEach((img, index) => {
    img.addEventListener('click', () => {
        showLightbox(index);
    });
});

function showLightbox(index) {
    currentImageIndex = index;
    lightboxImg.src = images[index].dataset.src;
    lightbox.classList.add('show');
    toggleControlsVisibility();
}

// function toggleControlsVisibility() {
//     if (images.length > 1) {
//         lightboxControls.style.display = 'flex';
//     } else {
//         lightboxControls.style.display = 'none';
//     }

//     if (currentImageIndex === 0) {
//         prevArrow.style.display = 'none';
//         nextArrow.style.display = 'block';
//     } else if (currentImageIndex === images.length - 1) {
//         prevArrow.style.display = 'block';
//         nextArrow.style.display = 'none';
//     } else {
//         prevArrow.style.display = 'block';
//         nextArrow.style.display = 'block';
//     }
// }

function closeLightbox() {
    lightbox.classList.remove('show');
}

function prevImage(event) {
    event.stopPropagation();
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
    lightboxImg.src = images[currentImageIndex].dataset.src;
    toggleControlsVisibility();
}

function nextImage(event) {
    event.stopPropagation();
    currentImageIndex = (currentImageIndex + 1) % images.length;
    lightboxImg.src = images[currentImageIndex].dataset.src;
    toggleControlsVisibility();
}

document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        closeLightbox();
    } else if (e.key === 'ArrowLeft' && lightbox.classList.contains('show')) {
        prevImage(e);
    } else if (e.key === 'ArrowRight' && lightbox.classList.contains('show')) {
        nextImage(e);
    }
});

toggleControlsVisibility(); // Initial visibility setup
