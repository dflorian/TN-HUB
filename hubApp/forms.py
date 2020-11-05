from django import forms
from .models import Paper, Backend

class PaperForm(forms.ModelForm):
	class Meta:
		model = Paper
		fields = ('title', 'category', 'author', 'description','keywords','link', 'backend')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Title of submission'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Authors'}),
			'category': forms.CheckboxSelectMultiple(),
			'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Description'}),
			'keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Keywords'}),
			'link': forms.TextInput(attrs={'class': 'form-control'}),
			'backend': forms.CheckboxSelectMultiple(),
		}
