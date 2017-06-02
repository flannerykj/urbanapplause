from django.contrib import admin
from .models import Musician
from .models import Artist


class MusicianAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['instruments']}),
    ]
    list_display = ('name', 'author')
    def save_model(self, request, obj, form, change):
    	obj.author = request.user
        obj.save()

admin.site.register(Musician, MusicianAdmin)

class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['style']}),
        (None,               {'fields': ['talent_type']}),
    ]
    list_display = ('name', 'author')
    def save_model(self, request, obj, form, change):
    	obj.author = request.user
        obj.save()

admin.site.register(Artist, ArtistAdmin)