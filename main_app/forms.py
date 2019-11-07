from .models import Profile, Restaurant, Menu
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
    
class ReservationCreateForm(forms.ModelForm):
	guest_num = forms.IntegerField()
	booking_date = forms.DateField()
	booking_time = forms.IntegerField()
	note = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':10}))

	class Meta:
		model = Reservation
		fields = ['guest_num', 'booking_date', 'booking_time', 'note']

class MenuForm(ModelForm):
  class Meta:
    model = Menu
    fields = ['name', 'price', 'description']