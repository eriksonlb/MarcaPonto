from django.shortcuts import render
from django.http import HttpResponse
import datetime

def login(request):
    return render(request, 'login.html')