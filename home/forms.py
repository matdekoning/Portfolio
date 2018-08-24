from django import forms
from .models import Article

class HomeForm(forms.Form):
    post = forms.CharField(max_length=100, label='Address:')
    huisOpp = forms.CharField(max_length=3, label='House area (m²):')
    perceelOpp = forms.CharField(max_length=4, label='Lot area (m²):')

class TwitterForm(forms.Form):
    post = forms.CharField(max_length=100, label='Enter word:')

class UploadImage(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['image']

