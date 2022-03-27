from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm

from .models import Student

# Create your views here.
def reg_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            #return redirect('home')
            return HttpResponse('Success!')
    else:
        form = StudentForm()
    return render(request, 'registration/regForm.html', {'form':form})

def index(request):
    return render(request,'registration/form.html',{'title': 'Регистрация'})

def print_list(request):
    students = Student.objects.all()
    res = '<h1>Список студентов</h1>'
    for i in students:
        res+=f'<div><p>{i.surname} {i.name}</p></div>'
    return HttpResponse(res)
