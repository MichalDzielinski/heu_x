(function () {
  const THRESHOLD = 55;
  let isExpanded = true;

  // --- Immediate helpers ---
  function applyShrunkImmediate() {
    gsap.set('.header-inner', { marginTop: '-5px', height: '100%' });
    gsap.set('.title-group', { paddingTop: 0, paddingBottom: -6 });
    gsap.set('.subheader', { opacity: 0, height: 0, overflow: 'hidden' });
    gsap.set('.title', { marginTop: -13, marginBottom: -25 });
    gsap.set('.logo', { scale: 0.68 });
    gsap.set('.sh1', { scale: 0.68 });
    gsap.set('.sh2', { scale: 0.68 });
    gsap.set('.title1', { scale: 0.75, x: -44 });

    // 🔹 NIE skalujemy elementu #nsd
    gsap.set('.nsd', { scale: 1 });

    gsap.set('.frm', { y: '-99px', duration: 0.5 });
    gsap.set('.lang', { y: '-125px' }); // lang zawsze ukryty przy shrink
  }

  function applyExpandedImmediate() {
    gsap.set('.header-inner', { marginTop: 'auto', height: 'auto' });
    gsap.set('.title-group', { paddingTop: 'auto', paddingBottom: 'auto' });
    gsap.set('.subheader', { opacity: 1, height: 'auto', overflow: 'visible' });
    gsap.set('.title', { marginTop: 'auto', marginBottom: 'auto' });
    gsap.set('.logo', { scale: 1 });
    gsap.set('.sh1', { scale: 1 });
    gsap.set('.sh2', { scale: 1 });
    gsap.set('.title1', { scale: 1, x: 0 });

    // 🔹 Upewniamy się, że #nsd pozostaje w naturalnej skali
    gsap.set('#nsd', { scale: 1 });

    gsap.set('.frm', { y: 0 });
    gsap.set('.lang', { y: 0 });
  }

  // --- Animate functions ---
  function animateToShrunk() {
    if (!isExpanded) return;
    const tl = gsap.timeline();
    tl.to('.header-inner', { marginTop: '-5px', height: '100%', duration: 0.2, ease: 'power2.out' })
      .to('.title-group', { paddingTop: -12, paddingBottom: -12, duration: 0.3 }, '<')
      .to('.subheader', { opacity: 0, height: 0, duration: 0.3, ease: 'power1.out' }, '<')
      .to('.title', { marginTop: -13, marginBottom: -25, duration: 0.5 }, '<')
      .to('.logo', { scale: 0.68, duration: 0.45 }, '<')
      .to('.sh1', { scale: 0.68, duration: 0.45 }, '<')
      .to('.sh2', { scale: 0.68, duration: 0.45 }, '<')
      .to('.title1', { scale: 0.75, x: -44, duration: 0.45 }, '<')
      .to(['.frm', '.ttp'], { y: -102, duration: 0.5 }, '<')
      // 🔹 Pomijamy animację skali dla #nsd
      // .to('#nsd', { scale: 1.05, duration: 0.2 }, '<')
      .to('.lang', { y: '-125px', duration: 0.5, ease: "power2.out" }, '<');
    isExpanded = false;
  }

  function animateToExpanded() {
    if (isExpanded) return;

    const tl = gsap.timeline();
    tl.to('.header-inner', { marginTop: 'auto', height: 'auto', duration: 0.01 })
      .to('.title-group', { paddingTop: 'auto', paddingBottom: 'auto', duration: 0.3 }, '<')
      .to('.subheader', { opacity: 1, height: 'auto', duration: 0.9 }, '<')
      .to('.title', { marginTop: 'auto', marginBottom: 'auto', duration: 1.0 }, '<')
      .to('.logo', { scale: 1, duration: 0.45 }, '<')
      .to('.sh1', { scale: 1, duration: 0.45 }, '<')
      .to('.sh2', { scale: 1, duration: 0.45 }, '<')
      .to('.title1', { scale: 1, x: 0, duration: 0.45 }, '<');
      // 🔹 #nsd bez zmiany skali, więc pomijamy

    gsap.to('.frm', {
      y: 0,
      duration: 0.7,
      ease: "power2.out",
      delay: 0.5,
      onUpdate: function () {
        const y = gsap.getProperty('.frm', 'y');
        if (y >= -0.5) {
          gsap.to('.lang', { y: 0, duration: 0.2, ease: "power2.out" });
        }
      },
      onComplete: function () {
        gsap.set('.lang', { y: 0 });
      }
    });

    isExpanded = true;
  }

  // --- Init ---
  function init() {
    const header = document.querySelector('#header');
    if (!header) return;

    header.style.overflow = 'hidden';
    const lang = header.querySelector('.lang');
    if (lang) lang.style.position = 'absolute';

    isExpanded = (window.scrollY <= THRESHOLD);
    if (isExpanded) applyExpandedImmediate();
    else applyShrunkImmediate();

    window.addEventListener('scroll', () => {
      if (window.scrollY > THRESHOLD) animateToShrunk();
      else animateToExpanded();
    }, { passive: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
