from __future__ import unicode_literals
import datetime
from django.utils import timezone
from geoposition.fields import GeopositionField
from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Musician(models.Model): 
	name = models.CharField(max_length=120)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	signup_date = models.DateTimeField(auto_now_add=True)
	bio = models.TextField(max_length=500, blank=True)
	def __str__(self):
		return self.name