from django.shortcuts import render, redirect
from home.settings import settings
import requests
from home.settings import settings

def education(request):
    return render(request, 'education.html')

def courses(request):
    dts = requests.get(settings.URL_ENV_COUSERS)
    dts = dts.json()
    context = {
        'dts': dts
    }
    return render(request, 'courses.html', context)

def course_item(request, id):
    db = requests.get(settings.URL_ENV_COUSERS + id + '/')
    aux = db.json()
    acts = aux['content'].split('\n')
    context = {
        'dts': aux,
        'acts': acts
    }
    return render(request, 'item_course.html', context)