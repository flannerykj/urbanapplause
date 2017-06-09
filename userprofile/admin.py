from django.contrib import admin
from django.contrib.gis.db import models
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin): 
	model = Profile
	fieldsets = [
        (None,               {'fields': ['musician']}),
    ]

admin.site.register(Profile, ProfileAdmin)