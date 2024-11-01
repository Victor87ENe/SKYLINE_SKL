from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.views.generic import View
# from . views import examportal,home, about
from.models import Student,CohortGroup,Student_Profile
import pdb
# Create your views here.


# pdb.set_trace()
def examportal(request):
    all_students = Student.objects.all()
    
    context = {
        'students': all_students  
    }
    
    return render(request,'home/index.html', context= context)


# def home(request):
    
#     return render(request,'home/index.html' )

def about(request):
    return render(request, 'about/about.html')

    
def student_profile(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    profile = get_object_or_404(Student_Profile, student=student)

    context = {
        'student': student,
        'profile': profile,
    }

    return render(request, 'student_profile.html', context)