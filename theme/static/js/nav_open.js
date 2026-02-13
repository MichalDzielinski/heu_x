document.addEventListener('DOMContentLoaded', () => {
  const nav = document.getElementById('small_nav');
  const navBtn = document.getElementById('navBtn');

  const navTimeline = gsap.timeline({ paused: true, reversed: true });

  // ustawienie startowe – tylko przesunięcie w poziomie
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

  navBtn.addEventListener('click', () => {
    navTimeline.reversed() ? navTimeline.play() : navTimeline.reverse();
  });
});
