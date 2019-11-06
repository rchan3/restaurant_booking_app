from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Restaurant
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
  return render(request, 'index.html')

def restaurants(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'restaurant/index.html', { 'restaurants': restaurants })

def restaurant_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  return render(request, 'restaurant/detail.html', { 'restaurant': restaurant })

class RestaurantCreate(LoginRequiredMixin, CreateView):
  model = Restaurant
  fields = ['name', 'location', 'max_capacity', 'opening_time', 'closing_time', 'description']

  def form_valid(self, form):
    form.instance.owner = self.request.user
    return super().form_valid(form)

  success_url = '/restaurants/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required(login_url='/auth/login/')
def dashboard(request):
  return render(request, 'user/dashboard.html')