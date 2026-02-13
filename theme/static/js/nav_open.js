function initNavbar() {
    const openBtn = document.getElementById('navbarOpen');
    const closeBtn = document.getElementById('navbarClose');
    const nav = document.getElementById('small_nav');

    if (!openBtn || !closeBtn || !nav) return;

    // zapobiega ponownej inicjalizacji tego samego elementu
    if (nav.dataset.initialized === "true") return;
    nav.dataset.initialized = "true";

    const navTimeline = gsap.timeline({ paused: true, reversed: true });

    navTimeline.set(nav, { 
        x: '200%', 
        autoAlpha: 0, 
        pointerEvents: 'none' 
    });

    navTimeline.to(nav, { 
        x: '0%', 
        autoAlpha: 0.97, 
        pointerEvents: 'auto', 
        duration: 0.8, 
        ease: 'power3.out' 
    });

    openBtn.addEventListener('click', () => { 
        if (navTimeline.reversed()) navTimeline.play(); 
    });

    closeBtn.addEventListener('click', () => { 
        if (!navTimeline.reversed()) navTimeline.reverse(); 
    });
}

// przy pierwszym ładowaniu
document.addEventListener('DOMContentLoaded', initNavbar);

// po każdym swapie HTMX
document.body.addEventListener('htmx:afterSwap', function () {
    initNavbar();
});