from django.contrib import admin
from .models import Sighting

# Register your models here.
class SightingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['artist']}),
        (None,               {'fields': ['location']}),
    ]
    list_display = ('artist', 'author', 'location', 'datetime')

admin.site.register(Sighting, SightingAdmin)