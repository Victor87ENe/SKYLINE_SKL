from django.urls import path
from . views import examportal,home, about
from . import views

urlpatterns = [
    path('', home, name="home"),

    path('about/', about, name='about'),
]
