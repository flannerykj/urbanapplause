from __future__ import unicode_literals
import json

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from geoposition.fields import GeopositionField
from django.conf import settings
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class InstrumentTag(TaggedItemBase):
    content_object = models.ForeignKey('Musician')

class GenreTag(TaggedItemBase):
    content_object = models.ForeignKey('Musician')

class MediumTag(TaggedItemBase):
    content_object = models.ForeignKey('Artist')

class StyleTag(TaggedItemBase):
    content_object = models.ForeignKey('Artist')

class Talent(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)
    talent_type = models.CharField(max_length=100)
    @property
    def get_type(self):
		return self.talent.get_type
    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def __str__(self):
		return self.name
	class Meta:
		abstract = True

class Musician(Talent):
	talent_type = "musician"
	instruments = TaggableManager(through=InstrumentTag, related_name='musician_instruments', verbose_name='instruments')
	genres = TaggableManager(through=GenreTag, related_name='musician_genre', verbose_name='genres')
	def get_absolute_url(self):
		return "/talent/musicians/%i/" % self.id
	def get_type(self):
		return "musician"
	@property
	def metadata(self):
		return {'instruments': map(str, self.instruments.names()),
				'genres': map(str, self.genres.names())
				}

class Artist(Talent):
	talent_type = "artist"
	medium = TaggableManager(through=MediumTag, related_name='artist_medium', verbose_name='medium')
	style = TaggableManager(through=StyleTag, related_name='artist_style', verbose_name='style')
	def get_absolute_url(self):
		return "/talent/artists/%i/" % self.id
	def get_type(self):
		return "artist"
	@property
	def metadata(self):
		return {'medium': map(str, self.medium.names()),
				'style': map(str, self.style.names())
				}
	