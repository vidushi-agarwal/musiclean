from django.db import models
from django import forms
from django.utils import timezone
# Create your models here.
class LyricModel(models.Model): #this is model 
    song_title =models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    
    def __str__(self):
        return self.song_title

class ReviewModel(models.Model):
    jingle=models.CharField(max_length=255)
    myreview = models.TextField(max_length=1000,blank=True)
    picture = models.ImageField(upload_to='posters_review')
    date_posted=models.DateField(default=timezone.now())
    def __str__(self):
        return self.jingle