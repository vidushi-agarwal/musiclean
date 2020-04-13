from django.shortcuts import render
from django.http import HttpResponse
from .forms import LyricModelForm
from .fin import lyric_class


# Create your views here.
def index(request):
    if (request.method == "POST"):
        lyrics = LyricModelForm(request.POST)  #lyrics is a form here
        if (lyrics.is_valid()):
            lyrics.save()
            song_title = lyrics.cleaned_data.get("song_title")
            artist=lyrics.cleaned_data.get("artist")
            selection = lyrics.cleaned_data.get("selection")
            lyric_class(artist,song_title).get_lyrics()
            return render(request,'handclean_app/index1.html',{'song_title':song_title,'artist':artist,'selection':selection})
            

    else:
        lyrics = LyricModelForm()
    return render(request, 'handclean_app/index.html', {'lyrics': lyrics})

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
    