from django.contrib import admin
from .models import Restaurant, Menu_Item
from .models import Profile

admin.site.register(Profile)
admin.site.register(Restaurant)
admin.site.register(Menu_Item)
