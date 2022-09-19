from django import forms
from .models import Podcast
from django.forms.widgets import DateInput


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__'
        widgets= {
            'Date':DateInput({'type':'date'})
        }