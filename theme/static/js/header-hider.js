(function () {
    const header = document.getElementById('header'); // your header
    const footer = document.getElementById('footer');    // your footer
    if (!header || !footer) return;
  
    let isFooterVisible = false;
  
    const observer = new IntersectionObserver((entries) => {
      const e = entries[0];
      if (e.isIntersecting && !isFooterVisible) {
        // Footer is visible -> hide header
        gsap.to(header, { y: '-100%', duration: 0.4, ease: 'power2.out' });
        isFooterVisible = true;
      } else if (!e.isIntersecting && isFooterVisible) {
        // Footer is out of view -> show header
        gsap.to(header, { y: '0%', duration: 0.4, ease: 'power2.out' });
        isFooterVisible = false;
      }
    }, { threshold: 0 });
  
    observer.observe(footer);
  })();
