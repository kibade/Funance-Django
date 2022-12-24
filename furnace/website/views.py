from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.


def welcome(request):
    f = open('Test.txt', 'w')
    f.write('test')
    f.close()
    return HttpResponse("Welcome to the vgnghfurnace page")
