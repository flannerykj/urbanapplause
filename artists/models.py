from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from geoposition.fields import GeopositionField
from django.conf import settings

class Artist(models.Model):
	INSTRUMENT_CHOICES = (
		('Unspecified', 'Unspecified'),
		('Guitar', 'Guitar'),
	    ('Violin', 'Violin'),
	    ('Drums', 'Drums'),
	    ('Keyboard', 'Keyboard'),
	    ('Voice', 'Voice'),
	)
	name = models.CharField(max_length=200)
	instrument = models.CharField(max_length=100, choices=INSTRUMENT_CHOICES, default='Unspecified')
	pub_date = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('artists', kwargs={'pk': self.pk})