from django.db import models
from django import forms
# Create your models here.
class LyricModel(models.Model): #this is model 
    song_title =models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    
    def __str__(self):
        return self.song_title