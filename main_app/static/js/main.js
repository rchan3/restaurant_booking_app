const restaurants = document.querySelectorAll('.restaurants-list_item');

restaurants.forEach(restaurant => {
  restaurant.addEventListener('mouseenter', () => {
    restaurant.childNodes[1].classList.add('darkOverlay');
  });

  restaurant.addEventListener('mouseleave', () => {
    restaurant.childNodes[1].classList.remove('darkOverlay');
  });
});

const yearSpan = document.querySelector('#year');
const d = new Date();
yearSpan.textContent = d.getFullYear();