from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from geoposition.fields import GeopositionField
from django.conf import settings
from django.utils.timezone import utc

# Create your models here.
class Sighting(models.Model):
	talent = models.ForeignKey('talent.Talent')
	location = GeopositionField()
	datetime = models.DateTimeField(auto_now_add=True, blank=True)
	author = models.ForeignKey(User)
	notes = models.CharField(max_length=400)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def get_time_diff(self):
	    if self.time_posted:
	        now = datetime.datetime.utcnow().replace(tzinfo=utc)
	        timediff = now - self.time_posted
	        return timediff.total_seconds()
	@property
	def get_type(self):
		return self.talent.get_type