from django.contrib import admin
from .models import Restaurant, Menu, Profile, Reservation
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Menu)
admin.site.register(Profile)
