    (function () {
      const THRESHOLD = 55;
      const MQ = '(min-width: 1280px)';
    
      const initialExpanded = (typeof window !== 'undefined') && (window.scrollY <= THRESHOLD);
      document.documentElement.classList.add(initialExpanded ? 'header-expanded' : 'header-shrunk');
    
      function createSentinel() {
        const s = document.createElement('div');
        s.className = 'header-sentinel';
        s.style.position = 'absolute';
        s.style.top = THRESHOLD + 'px';
        s.style.left = '0';
        s.style.width = '1px';
        s.style.height = '1px';
        s.style.pointerEvents = 'none';
        s.style.opacity = '0';
        document.body.appendChild(s);
        return s;
      }
    
      function applyShrunkImmediate() {
        gsap.set('.header-inner', { marginTop: '-5px', height: '100%' });
        gsap.set('.title-group', { paddingTop: 0, paddingBottom: -6 });
        gsap.set('.subheader', { opacity: 0, height: 0, overflow: 'hidden' });
        gsap.set('.title', { marginTop: -13, marginBottom: -25 });
        gsap.set('.logo', { scale: 0.68 });
        gsap.set('.sh1', { scale: 0.68 });
        gsap.set('.sh2', { scale: 0.68 });
        gsap.set('.title1', { scale: 0.75, x: -44 });
        gsap.set('.nsd', { scale: 0.9 });
        gsap.set('.lang', { y: '-125px' });
        gsap.set('.frm',  { y: '-99px', duration: 0.5 });
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
        gsap.set('.nsd', { scale: 1 });
        gsap.set('.frm', { y: 0 });
        gsap.set('.lang', { y: 0 });
      }
    
      function animateToShrunk() {
        gsap.to('.header-inner', { marginTop: '-5px', height: '100%', duration: 0.2, ease: 'power2.out' });
        gsap.to('.title-group', { paddingTop: -12, paddingBottom: -12, duration: 0.3 });
        gsap.to('.subheader', { opacity: 0, height: 0, duration: 0.3, ease: 'power1.out' });
        gsap.to('.title', { marginTop: -13, marginBottom: -25, duration: 0.5 });
        gsap.to('.logo', { scale: 0.68, duration: 0.45 });
        gsap.to('.sh1', { scale: 0.68, duration: 0.45 });
        gsap.to('.sh2', { scale: 0.68, duration: 0.45 });
        gsap.to('.title1', { scale: 0.75, x: -44, duration: 0.45 });
        // gsap.to('.nsd', { scale: 0.9, duration: 0.2 });
        gsap.to('.nsd', { scale: 1.05, duration: 0.2 });
        gsap.set('.lang', { y: '-125px', duration: 0.5, ease: "power2.out", overwrite: "auto" });
        gsap.to('.frm', { y: '-99px', duration: 0.5,  ease: "power2.out", overwrite: "auto" });
      }
    
      function animateToExpanded() {
        const tl = gsap.timeline();
    
        tl.to('.header-inner', { marginTop: 'auto', height: 'auto', duration: 0.01 })
          .to('.title-group', { paddingTop: 'auto', paddingBottom: 'auto', duration: 0.3 }, '<')
          .to('.subheader', { opacity: 1, height: 'auto',  duration: 0.9 }, '<')
          .to('.title', { marginTop: 'auto', marginBottom: 'auto', duration: 1.0 }, '<')
          .to('.logo', { scale: 1, duration: 0.45 }, '<')
          .to('.sh1', { scale: 1, duration: 0.45 }, '<')
          .to('.sh2', { scale: 1, duration: 0.45 }, '<')
          .to('.title1', { scale: 1, x: 0, duration: 0.45 }, '<')
          .to('.nsd', { scale: 1, duration: 0.2 }, '<')
          .to('.frm', { y: 0, duration: 0.7, delay: 0.3  }, '>')
          .to('.lang', { y: 0, duration:0.2, delay: 0.2,  ease: "power2.out" }, '>')
        //  
          // Show AFTER frm animation
      }
    
      function init() {
        if (!document.querySelector('#header')) return;
    
        if (!window.matchMedia(MQ).matches) {
          if (initialExpanded) applyExpandedImmediate();
          else applyShrunkImmediate();
          return;
        }
    
        if (initialExpanded) applyExpandedImmediate();
        else applyShrunkImmediate();
    
        const sentinel = createSentinel();
        let isExpanded = initialExpanded;
    
        const observer = new IntersectionObserver((entries) => {
          const e = entries[0];
          if (e && e.isIntersecting) {
            if (!isExpanded) {
              animateToExpanded();
              isExpanded = true;
            }
          } else {
            if (isExpanded) {
              animateToShrunk();
              isExpanded = false;
            }
          }
        });
    
        observer.observe(sentinel);
      }
    
      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
      } else {
        init();
      }
    })();

