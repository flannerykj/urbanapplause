from django.contrib import admin
from .models import Musician
from performances.admin import ParticipationInline


class MusicianAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = (ParticipationInline,)

admin.site.register(Musician, MusicianAdmin)