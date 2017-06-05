from django import forms
from .models import Performance, Applause, Participation
from musicians.models import Musician
from mapwidgets.widgets import GooglePointFieldWidget

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['location', 'musicians']
        widgets = {
		'location': GooglePointFieldWidget,
		}
	musicians = forms.ModelMultipleChoiceField(queryset=Musician.objects.all())