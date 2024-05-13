from django import forms
from .models import File


class FileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ['file']


class WordForm(forms.Form):
	word = forms.CharField()