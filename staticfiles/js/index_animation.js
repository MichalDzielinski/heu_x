function initScrollAnimations() {
  // Usuń poprzednie ScrollTriggery, żeby się nie duplikowały
  if (typeof ScrollTrigger !== "undefined") {
    ScrollTrigger.getAll().forEach(trigger => trigger.kill());
  }

  // Rejestracja pluginu (tylko jeśli nie jest zarejestrowany)
  if (typeof gsap !== "undefined" && gsap.core && gsap.registerPlugin) {
    gsap.registerPlugin(ScrollTrigger);
  }

  // Inicjalizacja Lenis
  const lenis = new Lenis();
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add((time) => {
    lenis.raf(time * 1000);
  });
  gsap.ticker.lagSmoothing(0);

  // Właściwa animacja
  const cards = gsap.utils.toArray(".card");

  cards.forEach((card, index) => {
    if (index < cards.length - 1) {
      const cardInner = card.querySelector(".card-inner");

      gsap.fromTo(
        cardInner,
        {
          y: "0%",
          z: 0,
          rotationX: 0,
        },
        {
          y: "-50%",
          z: -250,
          rotationX: 45,
          scrollTrigger: {
            trigger: cards[index + 1],
            start: "top 95%",
            end: "bottom 75%",
            scrub: true,
            pin: card,
            pinSpacing: false,
          },
        }
      );

      gsap.to(cardInner, {
        "--after-opacity": 1,
        scrollTrigger: {
          trigger: cards[index + 1],
          start: "top 75%",
          end: "top -25%",
          scrub: true,
        },
      });
    }
  });
}

// Uruchom po załadowaniu strony
document.addEventListener("DOMContentLoaded", initScrollAnimations);

// Uruchom ponownie po załadowaniu HTMX (np. po zmianie języka)
document.body.addEventListener("htmx:afterSwap", (event) => {
  // Możesz opcjonalnie sprawdzić, czy wymieniony fragment zawiera animację
  if (event.detail.target && event.detail.target.querySelector(".card")) {
    initScrollAnimations();
  }
});
