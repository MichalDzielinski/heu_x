document.addEventListener('DOMContentLoaded', () => {
  const nav = document.getElementById('small_nav');
  const openBtn = document.getElementById('navbarOpen');
  const closeBtn = document.getElementById('navbarClose');

  const navTimeline = gsap.timeline({ paused: true, reversed: true });

  // ustawienie startowe – przesunięcie w poziomie i brak interakcji
  navTimeline.set(nav, {
    x: '120%',
    autoAlpha: 0,
    pointerEvents: 'none'
  });

  // animacja wjazdu
  navTimeline.to(nav, {
    x: '0%',
    autoAlpha: 0.97,
    pointerEvents: 'auto',
    duration: 0.8,
    ease: 'power3.out'
  });

  // przycisk otwierający navbar
  openBtn.addEventListener('click', () => {
    if (navTimeline.reversed()) {
      navTimeline.play();
    }
  });

  // przycisk zamykający navbar
  closeBtn.addEventListener('click', () => {
    if (!navTimeline.reversed()) {
      navTimeline.reverse();
    }
  });
});
