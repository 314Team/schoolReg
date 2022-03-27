from statistics import mode
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    fathername = models.CharField(max_length=20,blank=True)

    mom = models.CharField(max_length=50,blank=True)
    momPhone = models.CharField(max_length=20)
    dad = models.CharField(max_length=50,blank=True)
    dadPhone = models.CharField(max_length=20)
    
    birhDate = models.DateField()
    sex = models.BooleanField(null=True) #0-f 1-m n-nonbin
    grade = models.SmallIntegerField()
    address = models.CharField(max_length=100)    
    photo = models.ImageField(upload_to='students/photo/%Y/%m/')
    additional = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)