document.addEventListener('DOMContentLoaded', () => {
    const openBtn = document.getElementById('navbarOpen');
    const closeBtn = document.getElementById('navbarClose');
    const nav = document.getElementById('small_nav');

    if (!openBtn || !closeBtn || !nav) return;

    const navTimeline = gsap.timeline({ paused: true, reversed: true });
    navTimeline.set(nav, { x: '200%', autoAlpha: 0, pointerEvents: 'none' });
    navTimeline.to(nav, { x: '0%', autoAlpha: 0.97, pointerEvents: 'auto', duration: 0.8, ease: 'power3.out' });

    const openHandler = () => { if (navTimeline.reversed()) navTimeline.play(); };
    openBtn.addEventListener('click', openHandler);
    openBtn.addEventListener('touchstart', openHandler);

    const closeHandler = () => { if (!navTimeline.reversed()) navTimeline.reverse(); };
    closeBtn.addEventListener('click', closeHandler);
    closeBtn.addEventListener('touchstart', closeHandler);
});
