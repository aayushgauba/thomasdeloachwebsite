from typing_extensions import Required
from django.db import models

# Create your models here.
class Podcast(models.Model):
    Title = models.TextField(unique = True)
    Date = models.DateField()
    Audio= models.FileField(upload_to='../podcasts')
    Summary = models.TextField()
    Description = models.TextField()

