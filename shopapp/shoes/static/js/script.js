// Add this CSS style to the script.js file
document.addEventListener('DOMContentLoaded', function() {
    const swiperElements = document.querySelectorAll('.swiper');

    swiperElements.forEach(function(swiperElement) {
        new Swiper(swiperElement, {
            loop: true,
            pagination: {
                el: '.swiper-pagination',
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
    });
});

// Add this CSS style to the script.js file
document.addEventListener('DOMContentLoaded', function() {
    const fadeOutElements = document.querySelectorAll('.fade-out');

    fadeOutElements.forEach(function(element) {
        element.style.opacity = '0';
        element.style.transition = 'opacity 1s ease-in-out';
    });
});
