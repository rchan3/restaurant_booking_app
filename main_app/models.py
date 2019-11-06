from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=100)
	first_name = models.CharField(max_length=50) 
	last_name = models.CharField(max_length=50)
	phone = models.IntegerField()
	createdAt = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.user.username
