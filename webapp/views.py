
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login

def home(request):
    return render(request, 'home.html')

