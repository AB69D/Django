from django import urls
from django.urls import path
from edu import views
urlpatterns = [
    path('skill/', views.skill, name="skill")
]
