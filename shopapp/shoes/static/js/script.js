// script.js
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