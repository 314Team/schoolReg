from django.forms import ModelForm
from django.db import models
from .models import Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        