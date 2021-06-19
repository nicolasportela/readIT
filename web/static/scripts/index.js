var burger = document.querySelector('#burger');
var nav = document.querySelector('#navbarMenuHero');
    
burger.addEventListener('click', () => {
    burger.classList.toggle('is-active');
    nav.classList.toggle('is-active');
});
