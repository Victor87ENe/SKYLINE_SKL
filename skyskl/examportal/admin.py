from django.contrib import admin
from .models import Student,Program,Student_Profile,CohortGroup

# Register your models here.



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','last_name','status']




@admin.register(Student_Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['student','date_of_birth', 'rating','date_join','address']


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['courses','grade','student']


@admin.register(CohortGroup)
class CohortGroupAdmin(admin.ModelAdmin):
    list_display = ['name','date_join',]

