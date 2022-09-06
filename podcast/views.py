from django.shortcuts import render

def podcastList(request):
    return render(request,'podcast/podcasts.html')
    