from .models import Profile, Restaurant, Menu

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileCreateForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'phone', 'location']

class MenuForm(ModelForm):
  class Meta:
    model = Menu
    fields = ['name', 'price', 'description']
