from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import LyricModelForm
from .fin import lyric_class
from .models import LyricModel


# Create your views here.
def index(request):
    if (request.method == "POST"):
        lyrics = LyricModelForm(request.POST)  #lyrics is a form here
        if (lyrics.is_valid()):
            song_title = lyrics.cleaned_data.get("song_title")
            artist=lyrics.cleaned_data.get("artist")
            if (lyric_class(artist, song_title).get_lyrics() == 404):
                messages.warning(request, 'Please correct your spellings.')
                return render(request, 'handclean_app/index.html', {'lyrics': lyrics})
            else:
                lyrics.save()
                return render(request, 'handclean_app/index1.html', {'song_title': song_title, 'artist': artist})


            

    else:
        lyrics = LyricModelForm()
    return render(request, 'handclean_app/index.html', {'lyrics': lyrics})

def comingsoon(request):
    return render(request,'handclean_app/comingsoon.html',{})

def johny(request):
    song_title = 'Johny Johny Yes Papa'
    artist='Nursery Rhymes Club'
    my_model = LyricModel(song_title=song_title, artist=artist)
    my_model.save()
    lyric_class(artist,song_title).get_lyrics()
    return render(request, 'handclean_app/index1.html', {'song_title': song_title, 'artist': artist})
def despacito(request):
    song_title = 'Despacito'
    artist='Luis Fonsi'
    my_model = LyricModel(song_title=song_title, artist=artist)
    my_model.save()
    lyric_class(artist,song_title).get_lyrics()
    return render(request, 'handclean_app/index1.html', {'song_title': song_title, 'artist': artist})

def ring(request):
    song_title = 'Ring‐a‐Ring o' 
    artist='Charlotte Gainsbourg'
    my_model = LyricModel(song_title=song_title, artist=artist)
    my_model.save()
    lyric_class(artist,song_title).get_lyrics()
    return render(request, 'handclean_app/index1.html', {'song_title': song_title, 'artist': artist})

def coldplay(request):
    song_title = 'Something just like this'
    artist='Coldplay'
    my_model = LyricModel(song_title=song_title, artist=artist)
    my_model.save()
    lyric_class(artist,song_title).get_lyrics()
    return render(request, 'handclean_app/index1.html', {'song_title': song_title, 'artist': artist})




import os
from django.conf import settings
from django.http import HttpResponse, Http404
import mimetypes

#download the image
def download(request):
    fl_path = settings.BASE_DIR +'/handclean_app/static/handclean_app/images/a.png'
    filename = 'poster.png'

    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    