from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from.models import Student,Student_Profile,CohortGroup
from django.urls import reverse
from django.core.paginator import Paginator
# import pdb

# Create your views here.


# pdb.set_trace()
def examportal(request):
    all_students = Student.objects.all()  
    context = {
        'students': all_students      
    }
    return render(request,'home/index.html', context= context)
def home(request):   
    return render(request,'home/index.html' )

def about(request):
    return render(request, 'about/about.html')

def student_profile(request,id):
    student = get_object_or_404(Student, id=id)
    profile = get_object_or_404(Student_Profile, student=student) 
    student_url = reverse('student_profile', kwargs={'id': student.id})
    context = {
        'student': student,
        'profile': profile,
    } 
    return render(request, 'student_profile/student_profile.html', context)
   
def student_list(request):
    students = Student.objects.all()  # Query your data
    paginator = Paginator(students, 3)  # Show 3 students per page

    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page object for the requested page

    context = {'page_obj': page_obj}
    return render(request, 'student_list.html', context)    


    
