from django.urls import path

from .views import *

urlpatterns = [
    #path('',index),
    path('',reg_form,name='reg_form'),
    path('list/',print_list),
]