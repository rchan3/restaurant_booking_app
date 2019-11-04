const restaurants = document.querySelectorAll('.restaurants-list_item');

restaurants.forEach(restaurant => {
  restaurant.addEventListener('mouseover', () => {
    console.log(restaurant.childNodes[1].classList)
    restaurant.childNodes[1].classList.add('darkOverlay');
  });

  restaurant.addEventListener('mouseout', () => {
    console.log(restaurant.childNodes[1].classList)
    restaurant.childNodes[1].classList.remove('darkOverlay');
  });
});

const yearSpan = document.querySelector('#year');
const d = new Date();
yearSpan.textContent = d.getFullYear();