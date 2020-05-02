from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="home"),
    path('download/', views.download, name="dwnld_page"),
    path('poster/<int:song_id>', views.poster, name="poster"),
    path('gallery/', views.comingsoon, name="gallery"),
    path('review/',views.review, name="review")
    
]