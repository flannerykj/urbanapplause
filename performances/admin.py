from django.contrib import admin
from .models import Performance, Participation
from mapwidgets.widgets import GooglePointFieldWidget
from django.contrib.gis.db import models

# Register your models here.
class ParticipationInline(admin.TabularInline):
    model = Participation
    extra = 1

class PerformanceAdmin(admin.ModelAdmin): 
	inlines = (ParticipationInline,)
	model = Performance
	formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }

admin.site.register(Performance, PerformanceAdmin)