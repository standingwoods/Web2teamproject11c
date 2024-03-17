from django.contrib import admin
from tenrr.models import UserProfile
from .models import Category

admin.site.register(UserProfile)
admin.site.register(Category)
