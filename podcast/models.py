from typing_extensions import Required
from django.db import models

# Create your models here.
class Podcast(models.Model):
    Date = models.DateField()
    Audio= models.FileField(upload_to='../podcasts')
    Summary = models.TextField()
    Description = models.TextField()
    Tag = models.CharField(max_length=30)

