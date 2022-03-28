from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('Hello World! It\'s a home page!')
    return render(request,'home/index.html',{'text':'This is home page!'})

def suc(request):
    return render(request, 'home/index.html',{'text':'Registration success!'})