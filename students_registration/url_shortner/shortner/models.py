from django.db import models

class url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=20)