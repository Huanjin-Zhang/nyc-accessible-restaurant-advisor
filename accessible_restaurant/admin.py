from django.contrib import admin
from .models import User, User_Profile, Restaurant_Profile

# Register your models here.

admin.site.register(User)
admin.site.register(User_Profile)
admin.site.register(Restaurant_Profile)