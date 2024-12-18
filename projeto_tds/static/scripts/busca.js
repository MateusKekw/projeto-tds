const username = document.getElementById('new');
username.addEventListener('input', (event) => {
    const value = formatString(event.target.value);

    const usernames = document.querySelectorAll('.amizadesnovas .amigo');
    const none = document.getElementById('no-results');

    let hasresults = false;

    usernames.forEach(amigo => {
        if(formatString(amigo.textContent.indexOf(value) !== -1)){
            amigo.style.display = 'flex';
            hasresults = true;
        } else {
            amigo.style.display = 'none';
        }
    })

    if(hasresults){
        none.style.display = 'none';
    } else {
        none.style.display = 'block';
    }
});

function formatString(value){
    return value.toLowerCase().trin();
}


/*document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.getElementById("carousel");
    const slides = Array.from(carousel.children);

    // Duplicar os slides para criar o efeito de loop
    slides.forEach((slide) => {
        const clone = slide.cloneNode(true);
        carousel.appendChild(clone);
    });

    // Configura a animação com JavaScript
    let speed = 1; // Velocidade de rolagem (ajuste conforme necessário)
    let position = 0;

    function animateCarousel() {
        position -= speed;
        carousel.style.transform = `translateX(${position}px)`;

        // Se o primeiro slide sair completamente da tela, reposiciona
        const firstSlideWidth = slides[0].offsetWidth + 20; // Slide + margem
        if (position <= -firstSlideWidth) {
            carousel.appendChild(carousel.firstElementChild);
            position += firstSlideWidth;
        }

        requestAnimationFrame(animateCarousel);
    }

    animateCarousel();
});*/