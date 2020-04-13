from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="home"),
    path('download/',views.download,name="dwnld_page")
]