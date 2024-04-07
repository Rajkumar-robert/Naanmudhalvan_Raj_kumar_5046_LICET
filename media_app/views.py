from django.shortcuts import render
from .models import Song

def indexPage(request):
    songs = Song.objects.all()
    return render(request,'media_app/index.html',{'songs':songs})