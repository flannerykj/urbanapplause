from django.contrib import admin
from .models import Applause

# Register your models here.
class ApplauseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['talent']}),
        (None,               {'fields': ['location']}),
        (None,               {'fields': ['comments']})
    ]
    list_display = ('talent', 'comments', 'user', 'location', 'pub_date')
    def save_model(self, request, obj, form, change):
    	obj.user = request.user
        obj.save()

admin.site.register(Applause, ApplauseAdmin)