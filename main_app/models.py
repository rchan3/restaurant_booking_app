from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    max_capacity = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(5)])
    opening_time = models.IntegerField(default=9,validators=[MinValueValidator(0),MaxValueValidator(24)])
    closing_time = models.IntegerField(default=23,validators=[MinValueValidator(0),MaxValueValidator(24)])

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
