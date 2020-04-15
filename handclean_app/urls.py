from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="home"),
    path('download/', views.download, name="dwnld_page"),
    path('johny/', views.johny, name="johny"),
    path('ring/', views.ring, name='ringa'),
    path('coldplay/', views.coldplay, name='coldplay'),
    path('despacito/', views.despacito, name='despacito'),
    path('gallery/', views.comingsoon, name="gallery"),
    path('review/',views.review, name="review")
    
]