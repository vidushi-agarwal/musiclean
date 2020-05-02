from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import LyricModelForm,ReviewModelForm
from .fin_2 import lyric_class
from .models import LyricModel, ReviewModel
from .functions import upload_to_cloudinary
from .test import check



# Create your views here.
def index(request):
    c=LyricModel.objects.count() #count of the songs found
    if (request.method == "POST"):
        lyrics = LyricModelForm(request.POST)  #lyrics is a form here
        if (lyrics.is_valid()):
            song_title = lyrics.cleaned_data.get("song_title")
            artist=lyrics.cleaned_data.get("artist")
            if (lyric_class(artist, song_title).get_lyrics() == 404):
                messages.warning(request, 'Please correct your spellings.')
                return render(request, 'handclean_app/index.html', {'lyrics': lyrics,"count":c})
            else:
                lyrics.save()
                c=c+1 # increasing count of the songs found
                return render(request, 'handclean_app/index1.html', {'song_title': song_title, 'artist': artist,'count':c, "nav_dict": check.do_it()})
    else:
        lyrics = LyricModelForm()
    return render(request, 'handclean_app/index.html', {'lyrics': lyrics,"count":c, "nav_dict": check.do_it()})


def review(request):
    c=LyricModel.objects.count()
    pr_form =ReviewModelForm()
    if request.method == 'POST':
        pr_form = ReviewModelForm(request.POST,request.FILES)
        if pr_form.is_valid():
            # pr_form.save() #I could have directly saved it, but cloudinary nhi hoga fir
            x = ReviewModel()
            x.jingle=pr_form.cleaned_data.get("jingle")
            x.myreview = pr_form.cleaned_data.get("myreview")
            file1 = request.FILES.get('picture')
            cloud_upload = upload_to_cloudinary(file1)
            x.char_pic = cloud_upload["url"]            
            x.save()
            messages.success(request, 'Thanks for your review!')
            return redirect('home')
    review_done = ReviewModel.objects.all().order_by('-date_posted')
    print(review_done)
    return render(request, 'handclean_app/review.html', {'review': pr_form,'review_done':review_done,'count':c, "nav_dict": check.do_it()})


def comingsoon(request):
    return render(request,'handclean_app/comingsoon.html',{})

def poster(request, song_id):
    c=LyricModel.objects.count()
    m=LyricModel.objects.filter(id=song_id)
    song_title = m[0].song_title
    artist=m[0].artist
    my_model = LyricModel(song_title=song_title, artist=artist)
    my_model.save()
    lyric_class(artist,song_title).get_lyrics()
    return render(request, 'handclean_app/index1.html', {'song_title': song_title, 'artist': artist,'count':c, "nav_dict": check.do_it()})

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
    