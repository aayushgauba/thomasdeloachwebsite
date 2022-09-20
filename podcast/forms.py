from django import forms
from .models import Podcast
from django.forms.widgets import DateInput


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ['Title', 'Date', 'upload', 'Summary', 'Description']
        widgets= {
            'Date':DateInput({'type':'date'})
        }