from django.contrib import admin
from .models import post

@admin.register(post)
class postModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
