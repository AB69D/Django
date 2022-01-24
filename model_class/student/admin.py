from django.contrib import admin
from .models import student

@admin.register(student)
class useradmin (admin.ModelAdmin):
    list_display = ('id', 'name','email','password')
