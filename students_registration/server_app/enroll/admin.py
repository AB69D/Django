from django.contrib import admin
from .models import student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','student_id', 'student_name','student_email','student_pass')
admin.site.register(student , StudentAdmin)