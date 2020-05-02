from django.db import models
from django import forms
from django.utils import timezone
# Create your models here.
class LyricModel(models.Model): #this is model 
    song_title =models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    
    def __str__(self):
        return self.song_title

class ReviewModel(models.Model): #here I added picture to get input type=file template from crispy and in the model it will be stored as url of image as char_pic, else I would have to write customised front end my own without crispy
    jingle= models.CharField(max_length=255)
    myreview = models.TextField(max_length=1000, blank=True)
    char_pic=  models.CharField(max_length = 1000,default="https://res.cloudinary.com/do8xzkgcs/image/upload/v1571618470/gbvmr9fwrwcz9xp0ycos.png")
    picture = models.ImageField(upload_to='posters_review')
    date_posted=models.DateField(default=timezone.now)
    def __str__(self):
        return self.jingle