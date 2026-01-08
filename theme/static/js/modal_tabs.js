document.addEventListener("DOMContentLoaded", function () {
    const tabButtons = document.querySelectorAll(".tab-button");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const targetTab = button.getAttribute("data-tab");

        // Hide all tab contents
        tabContents.forEach((content) => {
          content.classList.add("hidden");
        });

        // Remove active styles from all buttons
        tabButtons.forEach((btn) => {
          btn.classList.remove("border-blue-500", "text-blue-600");
        });

        // Show the selected tab content
        document.getElementById(targetTab).classList.remove("hidden");

        // Highlight the active button
        button.classList.add("border-blue-500", "text-blue-600");
      });
    });
  });