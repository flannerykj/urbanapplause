from __future__ import unicode_literals
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

from django.db import models


class PostTag(TaggedItemBase):
    content_object = models.ForeignKey('Post')


def blog_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'blog/post_{0}/featured-{1}'.format(instance.id, filename)

class Post(models.Model):
    title = models.CharField(max_length=100)
    featured_img = models.FileField(upload_to=blog_directory_path, max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    author = models.ForeignKey(User)
    body = models.TextField()
    category = models.ForeignKey('blog.Category')
    tags = TaggableManager(through=PostTag)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
       return self.title+', '+self.pub_date.strftime('%Y-%m-%d %H:%M')

    @models.permalink
    def get_absolute_url(self):
        return 'blog:post', (self.slug,)

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
       return self.title

    class Meta:
        verbose_name_plural = "categories"
