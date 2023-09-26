from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from . models import Students, Contactus, Course
from . forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    allCourses = Course.objects.all()
    return render(request, 'courses.html', {'allCourses':allCourses})

def coursedetails(request,slug):
    fullDetails = Course.objects.filter(slug=slug).first()
    context = {'fullDetails':fullDetails}
    return render(request, 'coursedetails.html', context)

def students(request):
    allstudents = Students.objects.all()
    return render(request, 'students.html', {'allstudents':allstudents})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, 'contact.html')
    