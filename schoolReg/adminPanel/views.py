from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Если вы это видите, значит чел ответственный за админку не сделал свою работу!')