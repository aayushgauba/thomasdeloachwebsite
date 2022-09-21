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

class PodcastUpdateForm(forms.Form):
    Title = forms.CharField(max_length=100)
    Date = forms.DateField(widget = DateInput({'type':'date'}))
    Summary = forms.CharField(widget=forms.Textarea)
    Description = forms.CharField(widget=forms.Textarea)

class PodcastFileForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ['id', 'Title', 'Date', 'upload', 'Summary', 'Description']
        widgets= {
            'Date':forms.HiddenInput(),
            'Title':forms.HiddenInput(),
            'Summary':forms.HiddenInput(),
            'Description':forms.HiddenInput(),
            'id':forms.HiddenInput()
        }