from django.shortcuts import render, redirect
from home.settings import settings

def education(request):
    return render(request, 'education.html')

def courses(request):
    return render(request, 'courses.html')