from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from . models import Students, Contactus
from . forms import ContactForm

# Create your views here.

def home(request):
    # return HttpResponse('This is home page')
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def courses(request):
    return render(request, 'courses.html')
def students(request):
    allstudents = Students.objects.all()
    return render(request, 'students.html', {'all':allstudents})
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request, 'contact.html')
    