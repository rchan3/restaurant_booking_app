from django import forms
from .models import Profile, Reservation
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileCreateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['first_name', 'last_name', 'phone', 'location']

class ReservationCreateForm(forms.ModelForm):
	guest_num = forms.IntegerField()
	booking_date = forms.DateField()
	booking_time = forms.IntegerField()
	note = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Reservation
		fields = ['guest_num', 'booking_date', 'booking_time', 'note']