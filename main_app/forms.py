from django.forms import ModelForm
from .models import Restaurant

class RestaurantForm(ModelForm):
  class Meta:
    model = Restaurant
    fields = ['name', 'location', 'max_capacity', 'opening_time', 'closing_time', 'description']