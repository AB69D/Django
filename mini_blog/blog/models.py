from django.db import models

class post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()