from __future__ import unicode_literals
from datetime import datetime, timedelta, tzinfo
import requests
from django.utils import timezone
from geoposition.fields import GeopositionField
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.contrib.gis.db import models
from geopy.geocoders import GoogleV3
from musicians.models import Musician
from django.contrib.auth.models import User

class InstrumentTag(TaggedItemBase):
    content_object = models.ForeignKey('Participation')

class GenreTag(TaggedItemBase):
    content_object = models.ForeignKey('Performance')

# Create your models here.
class Performance(models.Model): 
	musicians = models.ManyToManyField(Musician, through='Participation', null=True)
	audience = models.ManyToManyField(User, through='Applause', null=True)
	start_time = models.DateTimeField(auto_now_add=True)
	end_time = models.DateTimeField(null=True)
	location = models.PointField()
	genres = TaggableManager(through=GenreTag, related_name='genres', verbose_name='genres')
	def get_musicians(self):
		return map(str, self.musicians.all())
	def get_address(self):
		base = "http://maps.googleapis.com/maps/api/geocode/json?"
		params = "latlng={lat},{lon}&sensor=true".format(lat=self.location.y,lon=self.location.x)
		url = "{base}{params}".format(base=base, params=params)
		response = requests.get(url)
		return response.json()['results'][0].get('formatted_address')
	def __repr__(self):
		return str(self.id)
	def _str_(self): 
		return "performance"
	@property
	def total_audience(self):
		return self.audience.count()

class Participation(models.Model): 
	musician = models.ForeignKey(Musician)
	performance = models.ForeignKey(Performance)
	instruments = TaggableManager(through=InstrumentTag, related_name='instruments', verbose_name='instruments')

class Applause(models.Model): 
	user = models.ForeignKey(User)
	performance = models.ForeignKey(Performance)
	datetime = models.DateTimeField(auto_now_add=True)
