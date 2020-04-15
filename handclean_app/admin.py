from django.contrib import admin
from .models import LyricModel,ReviewModel


# Register your models here.

class LyricAdmin(admin.ModelAdmin):
    list_display=('song_title','artist')


admin.site.register(LyricModel, LyricAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display=('jingle','myreview','date_posted')


admin.site.register(ReviewModel,ReviewAdmin)