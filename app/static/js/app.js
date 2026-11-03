new Swiper('.slider-swiper', {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});

new Swiper('.last-events-swiper', {
    slidesPerView: 1,
    spaceBetween: 10,
    breakpoints: {
        640: {
            slidesPerView: 1,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 2,
            spaceBetween: 20,
        },
        1024: {
            slidesPerView: 3,
            spaceBetween: 10,
        },
        1400: {
            slidesPerView: 4,
            spaceBetween: 10,
        },
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});

new Swiper('.gallery-swiper', {
    slidesPerView: 3,
    grid: {
        rows: 2,
        fill:'row'
    },
    navigation: {
        nextEl: '.gallery-next',
        prevEl: '.gallery-prev',
    },
    spaceBetween: 30,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
});