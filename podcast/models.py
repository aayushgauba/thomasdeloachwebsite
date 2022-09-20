from typing_extensions import Required
from django.db import models

# Create your models here.
class Podcast(models.Model):
    Title = models.CharField(unique = True, max_length=100, blank=False)
    Date = models.DateField(blank=False)
    upload= models.FileField(upload_to='podcasts', blank=False)
    Summary = models.TextField(blank=False)
    Description = models.TextField(blank=False)
    Delete = models.BooleanField(default=False)
