from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    max_capacity = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(5)])
    opening_time = models.IntegerField(default=9,validators=[MinValueValidator(0),MaxValueValidator(24)])
    closing_time = models.IntegerField(default=23,validators=[MinValueValidator(0),MaxValueValidator(24)])
    description = models.CharField(default="",max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})

class Menu_Item(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=100)
	first_name = models.CharField(max_length=50) 
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	phone = models.IntegerField()
	createdAt = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return first_name + " " + last_name
