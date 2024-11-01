from django.urls import path
# from . views import examportal,home, about
from . import views

# urlpatterns = [
#     path('', home, name="home"),
    
#     path('about/', about, name='about'),
# ]


urlpatterns = [
    path('', views.examportal, name='examportal'),
    
    path('about/', views.about, name='about'),

    path('student/<int:student_id>/', views.student_profile, name='student_profile'),
]