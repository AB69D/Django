from django.urls import path
from . import views

urlpatterns = [
    path('coursedj/',views.learn_django),
    path('coursepy/', views.learn_python, name = 'course_page'),

]
