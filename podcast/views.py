from django.shortcuts import render, redirect
from .models import Podcast

def podcastList(request):
    podcasts =  Podcast.objects.filter(Delete=False)
    return render(request,'podcast/podcasts.html',context={'podcasts':podcasts})

def podcastView(request, podcast_id):
    podcast =  Podcast.objects.get(id = podcast_id)
    return render(request,'podcast/podcast.html',context={'podcast':podcast})

def Delete(request, podcast_id):
    if(request.method == 'POST'):
        podcast = Podcast.objects.get(id = podcast_id)
        if(podcast.Delete == True):
            podcast.delete()
            return redirect('recycle')

        else:
            podcast.Delete = True
            podcast.save()
            return redirect('dashboard')