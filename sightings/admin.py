from django.contrib import admin
from .models import Sighting

# Register your models here.
class SightingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['artist']}),
        (None,               {'fields': ['location']}),
    ]
    list_display = ('artist', 'author', 'location', 'datetime')
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Sighting, SightingAdmin)