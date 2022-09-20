from django.shortcuts import render
from .models import Podcast

def podcastList(request):
    podcasts =  Podcast.objects.all()
    return render(request,'podcast/podcasts.html',context={'podcasts':podcasts})

def podcastView(request, podcast_id):
    podcast =  Podcast.objects.get(id = podcast_id)
    return render(request,'podcast/podcast.html',context={'podcast':podcast})
