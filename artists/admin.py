from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['instrument']}),
    ]
    list_display = ('name', 'author')
    def save_model(self, request, obj, form, change):
    	obj.author = request.user
        obj.save()

admin.site.register(Artist, ArtistAdmin)