from .models import Profile, Restaurant, Reservation, Menu
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileCreateForm, UserUpdateForm, ReservationCreateForm, MenuForm

def home(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'index.html', {'restaurants': restaurants})

def restaurants(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'restaurant/index.html', { 'restaurants': restaurants })

def restaurant_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  form = ReservationCreateForm()
  menu_form = MenuForm()
  location = restaurant.location.replace(" ","+")
  return render(request, 'restaurant/detail.html', { 'restaurant': restaurant, 'menu_form': menu_form, 'location':location, 'reservationForm': form })

def add_menu(request, restaurant_id):
    form = MenuForm(request.POST)
    if form.is_valid():
      new_menu = form.save(commit=False)
      new_menu.restaurant_id = restaurant_id
      new_menu.save()
    return redirect('rdetail', restaurant_id=restaurant_id)

class RestaurantCreate(LoginRequiredMixin, CreateView):
  model = Restaurant
  template_name = 'restaurant/new.html'
  fields = ['name', 'location', 'max_capacity', 'opening_time', 'closing_time', 'description']

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

  success_url = '/restaurants/'

def signup(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      Profile.objects.create(user_id=user.id)
      # username = form.cleaned_data('username')
      messages.success(request, "signup was successful...")
      return redirect('/auth/login/')
  else:
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserRegisterForm()
  context = {'form': form}
  return render(request, 'registration/signup.html', context)

@login_required
def dashboard(request):
  user_reservations = Reservation.objects.filter(customer=request.user)
  user_restaurants = Restaurant.objects.filter(owner=request.user)
  usr_form = UserUpdateForm(instance=request.user)
  p_form = ProfileCreateForm(instance=request.user.profile) 
  context = { 'userForm': usr_form, 'profileForm': p_form, "restaurants": user_restaurants, 
  "reservations": user_reservations}
  return render(request, 'user/dashboard.html', context)

@login_required
def update_user_info(request):
  # usr_form = UserUpdateForm(request.POST, instance=request.user)
  if request.method == 'POST':
    usr_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileCreateForm(request.POST, instance=request.user.profile)
    if usr_form.is_valid() and p_form.is_valid():
      user_form = usr_form.save()
      prof_form = p_form.save()

      messages.success(request, "Profile update was successful...")
    return redirect('user_dashboard')

@login_required
def create_reservation(request, restaurant_id):
  form = ReservationCreateForm(request.POST)
  restaurant = Restaurant.objects.get(id=restaurant_id)
  
  if form.is_valid():
    reservation_data = form.cleaned_data
    if restaurant.is_space_available(reservation_data):
      updated_capacity = restaurant.update_capacity(reservation_data)
      new_reservation = form.save(commit=False)
      new_reservation.customer = request.user
      new_reservation.restaurant = restaurant
      new_reservation.save()
      restaurant.save()
      messages.success(request, "Your reservation has been received.")
      return redirect(f'/restaurants/{restaurant_id}/')
    else:
      messages.error(request, "Reservation currently not accepted by this restaurant.")
      return redirect(f'/restaurants/{restaurant_id}/')
    
    