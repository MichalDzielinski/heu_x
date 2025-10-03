    function openContact() {
    modal = document.getElementById('contact-modal')
    overlay = document.getElementById('contact-overlay')
    // shrink_image = document.getElementById('shrink-image_'+id);

    


    overlay.classList.remove('hidden');
    modal.classList.remove('hidden');
    

    tl1 = gsap.timeline()

    gsap.set(overlay, { backgroundColor: "rgba(0, 0, 0, 0)", });
    gsap.set(modal, { opacity: 1, x: '250%' });

    tl1.to(overlay, {
                    backgroundColor: "rgba(69, 69, 69, 0.8)",
                    // opacity:1,
                    duration: 1,         
                    ease: "power2.out"}, '>')
    
    
    .to(modal, {
                    x: '105%', 
                    duration: 1.1, 
                    ease: "back.out", 
                      },">")

    modal.gsapTimeline = tl1

    document.onkeydown = function(e){
        if(e.key === 'Escape'){
            closeContact()
        }
    }

  }

  function closeContact() {
    modal  = document.getElementById('contact-modal')
    // overlay  = document.getElementById('overlay_' + id)
    const tl = modal.gsapTimeline;

    if (tl){
        tl.reverse().eventCallback('onReverseComplete', () => {
            modal.classList.add('hidden');
            overlay.classList.add('hidden');

        })
    }


  }

  