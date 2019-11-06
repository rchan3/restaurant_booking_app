from .models import Profile
from .models import Restaurant
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileCreateForm, UserUpdateForm

def home(request):
  return render(request, 'index.html')

def restaurants(request):
  restaurants = Restaurant.objects.all()
  return render(request, 'restaurant/index.html', { 'restaurants': restaurants })

def signup(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      username = form.cleaned_data('username')
      messages.success(request, f"{username} signup was successful...")
      return redirect('auth/login/')
  else:
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserRegisterForm()
    context = {'form': form}
  return render(request, 'registration/signup.html', context)

@login_required
def dashboard(request):
  if request.method == 'POST':
    usr_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileCreateForm(request.POST)

    if usr_form.is_valid() and p_form.is_valid():
      user_form = usr_form.save()
      profile = Profile.objects.create(user_id=request.user.id, 
        phone = p_form.cleaned_data['phone'], 
        location=p_form.cleaned_data['location'],
        first_name = p_form.cleaned_data['first_name'],
        last_name = p_form.cleaned_data['last_name']
      )

      messages.success(request, "Profile update was successful...")
      return redirect('user_dashboard')
  else:
    p_form = ProfileCreateForm(instance=request.user.profile)
    usr_form = UserUpdateForm(instance=request.user)
    context = { 'userForm': usr_form, 'profileForm': p_form}
    return render(request, 'user/dashboard.html', context)
