from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

# Create your views here.
def index(request):
    return render(request,'registration/form.html',{'title': 'Регистрация'})

def print_list(request):
    students = Student.objects.all()
    res = '<h1>Список студентов</h1>'
    for i in students:
        res+=f'<div><p>{i.surname} {i.name}</p></div>'
    return HttpResponse(res)
