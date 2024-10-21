from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from.models import Student,CohortGroup,Student_Profile,Program
import pdb
# Create your views here.


# pdb.set_trace()
def examportal(request):
    all_students = Student.objects.all()
    # print(all_students) 
    context = {
        'studen':all_students
    }
    
    return render(request,'home/index.html', context = context, )


def home(request):
    return render(request,'home/index.html')

def about(request):
    return render(request, 'about/about.html')

    
