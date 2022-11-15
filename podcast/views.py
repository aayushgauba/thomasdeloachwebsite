from django.shortcuts import render, redirect
from .models import Podcast

def podcastList(request):
    podcasts =  Podcast.objects.filter(Delete=False)
    return render(request,'podcast/podcasts.html',context={'podcasts':podcasts})

def podcastView(request, podcast_id):
    podcast =  Podcast.objects.get(id = podcast_id)
    return render(request,'podcast/podcast.html',context={'podcast':podcast})

def deleteall(request):
    if(request.method == 'POST'):
        podcasts = Podcast.objects.filter(Delete = True)
        for podcast in podcasts:
            podcast.delete()
        return redirect('recycle')

def restore(request, podcast_id):
    podcast = Podcast.objects.get(id = podcast_id)
    podcast.Delete = False
    podcast.save()
    return redirect('recycle')

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

def search(request):
    podcast = Podcast.objects.all()
    if 'hide' in request.GET:
        keywords = request.GET.get('hide')
        if keywords:
            podcast = Podcast.objects.filter(Title_icontains = keywords)
    return render(request, "admin/recycle.html", context = {'podcast':podcast})