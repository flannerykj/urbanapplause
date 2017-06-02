from django import forms
from models import Musician
from models import Artist
from taggit.forms import *

class MusicianForm(forms.ModelForm):
	class Meta:
		model = Musician
		fields = ['name', 'instruments', 'genres']

class ArtistForm(forms.ModelForm):
	class Meta:
		model = Artist
		fields = ['name', 'medium', 'style']