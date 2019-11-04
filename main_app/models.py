from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    max_capacity = models.IntegerField()
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(5)])
    opening_time = models.IntegerField(default=9,validators=[MinValueValidator(0),MaxValueValidator(24)])
    closing_time = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(24)])
