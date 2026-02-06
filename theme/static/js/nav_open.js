document.addEventListener('DOMContentLoaded', () => {
  const nav = document.getElementById('small_nav');
  const navBtn = document.getElementById('navBtn');

  const navTimeline = gsap.timeline({ paused: true, reversed: true });

  // ustawienie startowe: nad ekranem + niewidoczny
  navTimeline.set(nav, {
    y: '10%',
    x: '250%',
    autoAlpha: 0,       // opacity + visibility
    pointerEvents: 'none'
  });

  // animacja wjazdu
  navTimeline.to(nav, {
    x: '5%',
    autoAlpha: 0.97,    // fade in
    pointerEvents: 'auto',
    duration: 0.8,
    ease: 'power3.out'
  });

  // toggle po kliknięciu
  navBtn.addEventListener('click', () => {
    navTimeline.reversed() ? navTimeline.play() : navTimeline.reverse();
  });
});

