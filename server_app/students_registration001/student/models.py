from django.db import models

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
