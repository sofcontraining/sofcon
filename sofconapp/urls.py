from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('courses',views.courses,name='courses'),
    path('students',views.students,name='students'),
    path('contact',views.contact,name='contact'),
]