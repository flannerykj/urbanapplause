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
from geopy.geocoders import Nominatim

class InstrumentTag(TaggedItemBase):
    content_object = models.ForeignKey('Participation')

class GenreTag(TaggedItemBase):
    content_object = models.ForeignKey('Performance')

# Create your models here.
class Performance(models.Model): 
	musicians = models.ManyToManyField(Musician, through='Participation', null=True)
	audience = models.ManyToManyField(User, through='Applause', null=True)
	start_time = models.DateTimeField(auto_now_add=True, editable=True)
	end_time = models.DateTimeField(default=(datetime.now()+timedelta(hours=4)), null=True)
	location = models.PointField()
	genres = TaggableManager(through=GenreTag, related_name='genres', verbose_name='genres')
	def get_musicians(self):
		return self.participation_set.all()
	@property
	def total_audience(self):
		return self.audience.count()
	def get_address(self):
		geolocator = Nominatim()
		latlong = [str(self.location.y), str(self.location.x)]
		point = ", ".join(latlong)
		location = geolocator.reverse(point)
		return location.address

class Participation(models.Model): 
	musician = models.ForeignKey(Musician)
	performance = models.ForeignKey(Performance)
	instruments = TaggableManager(through=InstrumentTag, related_name='instruments', verbose_name='instruments')

class Applause(models.Model): 
	user = models.ForeignKey(User)
	performance = models.ForeignKey(Performance)
	datetime = models.DateTimeField(auto_now_add=True)
