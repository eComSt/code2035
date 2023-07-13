from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hw(request):
    return HttpResponse("Домашка по 4 занятию")