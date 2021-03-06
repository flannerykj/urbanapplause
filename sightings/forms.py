from django import forms
from django.forms import ModelChoiceField
from models import Sighting
from talent.models import Artist
from talent.models import Musician
from talent.models import Talent

class SightingForm(forms.ModelForm):
	CHOICES=[('artist','Artist'),
         ('musician','Musician')]
	talent_type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
	talent = forms.ModelChoiceField(queryset=Talent.objects.all(), to_field_name="name")

	def __init__(self, talent_type=None, *args, **kwargs):
		super(SightingForm, self).__init__(*args, **kwargs)
		self.fields['talent'] = forms.ModelChoiceField(
            queryset=Talent.objects.filter(talent_type=talent_type.encode("ascii"))
        )
		self.fields['talent'].label_from_instance = self.label_from_instance
	@staticmethod
	def label_from_instance(obj):
		return obj.name
	class Meta:
		model = Sighting
		fields = ['talent_type', 'talent', 'location', 'notes']
