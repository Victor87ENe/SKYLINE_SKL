from django.urls import path
from . import views



urlpatterns = [
    path('', views.examportal, name='examportal'), 
    path('about/', views.about, name='about'),
    path('student/<int:id>/', views.student_profile, name='student_profile'),
    # path('student/<str:username>/', views.student_profile, name='student_profile'),
]