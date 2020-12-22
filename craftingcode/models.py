from django.db import models

# Create your models here.

class Courses(models.Model):
    coursename = models.CharField(max_length=30)
    courseimage = models.ImageField(upload_to = 'pic')
    coursedesc = models.TextField()
    courseprice = models.IntegerField()
    