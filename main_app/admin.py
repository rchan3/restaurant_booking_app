from django.contrib import admin
from .models import Restaurant, Menu_Item, Profile
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Menu_Item)
admin.site.register(Profile)
