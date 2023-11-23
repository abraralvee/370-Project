from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse('Hello World')

