from django.urls import path
# from . views import examportal,home, about
from . import views

# urlpatterns = [
#     path('', home, name="home"),
    
#     path('about/', about, name='about'),
# ]


urlpatterns = [
    path('', views.examportal, name='examportal'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]