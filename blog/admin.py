from django.contrib import admin
from .models import Post
from .models import Category
from django.utils.text import slugify
from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['author']}),
        (None,               {'fields': ['pub_date']}),
        (None,               {'fields': ['updated']}),
        (None,               {'fields': ['featured_img']}),
        (None,               {'fields': ['body']}),
        (None,               {'fields': ['category']}),
        (None,               {'fields': ['tags']}),
        (None,               {'fields': ['slug']}),
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('author', 'pub_date', 'updated')

    def save_model(self, request, obj, form, change):
    	obj.author = request.user
        obj.save()
        
        return obj

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None,               {'fields': ['slug']}),
        (None,               {'fields': ['description']}),
    ]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)