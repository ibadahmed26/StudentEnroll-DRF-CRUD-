from django.contrib import admin
from .models import StudentModel, TeacherModel


@admin.register(StudentModel)
class StuAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','city','age','roll','date','teacher']


@admin.register(TeacherModel)
class StuAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','city','age','salary','join_date']
