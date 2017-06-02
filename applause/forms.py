from django import forms
from django.forms import ModelChoiceField
from models import Applause
from talent.models import Artist
from talent.models import Musician
from talent.models import Talent

class ApplauseForm(forms.ModelForm):
	talent = forms.ModelChoiceField(queryset=Talent.objects.all(), to_field_name="name")
	def __init__(self, talent_type=None, *args, **kwargs):
		super(ApplauseForm, self).__init__(*args, **kwargs)
		self.fields['talent'] = forms.ModelChoiceField(
            queryset=Talent.objects.filter(talent_type=talent_type.encode("ascii"))
        )
		self.fields['talent'].label_from_instance = self.label_from_instance
	@staticmethod
	def label_from_instance(obj):
		return obj.name
	class Meta:
		model = Applause
		fields = ['talent', 'location', 'comments']