from __future__ import unicode_literals
from django.db import models
from talent.models import Talent
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from geoposition.fields import GeopositionField
from django.conf import settings
from django.utils.timezone import utc
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class InstrumentTag(TaggedItemBase):
    content_object = models.ForeignKey('Applause')

class GenreTag(TaggedItemBase):
    content_object = models.ForeignKey('Applause')

class MediumTag(TaggedItemBase):
    content_object = models.ForeignKey('Applause')

class StyleTag(TaggedItemBase):
    content_object = models.ForeignKey('Applause')

class Applause(models.Model): 
	user = models.ForeignKey(User)
	talent = models.ForeignKey(Talent)
	pub_date = models.DateTimeField(auto_now_add=True)
	comments = models.CharField(max_length=200)
	location = GeopositionField()
	instruments = TaggableManager(through=InstrumentTag, related_name='ms_instruments', verbose_name='instruments')
	genres = TaggableManager(through=GenreTag, related_name='ms_genres', verbose_name='genres')
	style = TaggableManager(through=StyleTag, related_name='gf_style', verbose_name='style')
