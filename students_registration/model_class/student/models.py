from django.db import models
from django.forms import widgets

class student(models.Model):
    name = models.CharField(max_length=20)
    email =  models.EmailField(blank=True,max_length=70)
    password = models.CharField(max_length=100)
