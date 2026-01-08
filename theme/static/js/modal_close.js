
function openModal(id) {
    modal = document.getElementById('modal-' + id)
    overlay = document.getElementById('overlay_' + id)
    // shrink_image = document.getElementById('shrink-image_'+id);
    flp = document.getElementById('flip-card-'+id);

    let flipped = false;


    overlay.classList.remove('hidden');
    modal.classList.remove('hidden');
    flipped = !flipped;

    tl1 = gsap.timeline()

    gsap.set(overlay, { backgroundColor: "rgba(0, 0, 0, 0)", });
    gsap.set(modal, { opacity: 1, x: '140%' });

    tl1.to(flp, {
      rotateY: flipped ? 180 : 0 ,
      duration: 1,
      ease: "power1.inOut", }, ).to(overlay, {
                    backgroundColor: "rgba(69, 69, 69, 0.8)",
                    // opacity:1,
                    duration: 3,         
                    ease: "power2.out", delay:1}, '<')
            .to(modal, {
                    x: 0, 
                    duration: 3.0, 
                    ease: "power3.out", 
                    delay: 0.9  },"<")

    modal.gsapTimeline = tl1

    document.onkeydown = function(e){
        if(e.key === 'Escape'){
            closeModal(id)
        }
    }

  }

  function closeModal(id) {
    modal  = document.getElementById('modal-' + id)
    // overlay  = document.getElementById('overlay_' + id)
    const tl = modal.gsapTimeline;

    if (tl){
        tl.reverse().eventCallback('onReverseComplete', () => {
            modal.classList.add('hidden');
            overlay.classList.add('hidden');

        })
    }}


