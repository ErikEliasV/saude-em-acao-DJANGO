document.addEventListener("DOMContentLoaded",function(){Promise.all(Array.from(document.images).map(e=>e.complete?Promise.resolve():new Promise(o=>{e.onload=e.onerror=o}))).then(()=>{new Swiper(".swiper",{autoplay:{delay:2500,disableOnInteraction:!1},grabCursor:!0,centeredSlides:!0,slidesPerView:"auto",keyboard:{enabled:!0},mousewheel:{thresholdDelta:70},spaceBetween:10,loop:!0,loopAdditionalSlides:1,breakpoints:{640:{slidesPerView:2,spaceBetween:20},1024:{slidesPerView:3,spaceBetween:30}},coverflowEffect:{rotate:0,stretch:0,depth:0,modifier:1,slideShadows:!1}})})});