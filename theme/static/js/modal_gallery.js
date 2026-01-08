document.querySelectorAll('.gallery').forEach(grid => {
    grid.addEventListener('click', (e) => {
      const clicked = e.target.closest('.gs_el');
      const main = grid.querySelector('.main-img'); // tylko w obrębie danej galerii
      
      if (!clicked || clicked === main) return;
      
      const state = Flip.getState(grid.querySelectorAll('.gs_el'));
      
      // Zamiana klas
      main.classList.remove('col-span-2', 'row-span-2', 'main-img');
      clicked.classList.add('col-span-2', 'row-span-2', 'main-img');
      
      // Zamiana pozycji w gridzie
      grid.insertBefore(clicked, main);
      grid.appendChild(main);
      
      // Animacja
      Flip.from(state, {
        duration: 0.6,
        ease: 'power1.inOut'
      });
    });
  });