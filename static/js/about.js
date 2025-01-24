document.addEventListener("DOMContentLoaded", () => {
    const imageButton = document.getElementById("imageButton");
    const imageModal = document.getElementById("imageModal");
    const closeImageModal = document.getElementById("closeImageModal");
  
    imageButton.addEventListener("click", () => {
      imageModal.classList.remove("hidden");
      imageModal.classList.add("flex");
    });
  
    closeImageModal.addEventListener("click", () => {
      imageModal.classList.add("hidden");
      imageModal.classList.remove("flex");
    });
  });
  