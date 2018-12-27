from django import forms
from .models import AppDetails

class AppDetailForm(forms.ModelForm):
	class Meta:
		model = AppDetails
		fields = ['userId', 'app', 'timestamp']
	