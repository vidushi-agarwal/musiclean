from django import forms
from .models import LyricModel


# This is a model form- this is created using model
class LyricModelForm(forms.ModelForm):
    choice = [
        ("soap_value", "soap"),
        ("sanitizer_value","sanitizer")
    ]
    selection = forms.ChoiceField(choices=choice, widget=forms.RadioSelect)
    
    class Meta:
        model = LyricModel
        fields={'song_title','artist','selection'}

