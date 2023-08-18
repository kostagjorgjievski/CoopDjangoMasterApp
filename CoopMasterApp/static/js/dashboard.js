document.addEventListener('DOMContentLoaded', function() {
    const closeButton = document.querySelector('button[type="button"]');
    const offCanvasMenu = document.querySelector('.relative.z-50.lg:hidden');
  
    closeButton.addEventListener('click', function() {
      offCanvasMenu.style.display = offCanvasMenu.style.display === 'none' ? '' : 'none';
    });
  });