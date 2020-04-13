from django.contrib import admin
from .models import LyricModel


# Register your models here.

class LyricAdmin(admin.ModelAdmin):
    list_display=('song_title','artist')


admin.site.register(LyricModel,LyricAdmin)