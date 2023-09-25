from django.db import models

## Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    course = models.CharField(max_length=250)

    def __str__(self):
        return self.name + ' - ' + self.course

## Contact Us Table
class Contactus(models.Model):
    name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    course = models.CharField(max_length=250)
    comment = models.CharField(max_length=250)

    def __str__(self):
        return self.name + ' - ' + self.course

## Courses Table
class Course(models.Model):
    sno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=255)
    csummary = models.TextField()
    cimg = models.ImageField(upload_to='courseimages')
    heading = models.CharField(max_length=100)
    slug = models.SlugField(max_length=500)

    def __str__(self):
        return self.cname