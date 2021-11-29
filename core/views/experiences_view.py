from django.shortcuts import render
import requests
from requests.models import Response
from home.settings import settings

def list_experiences(request):
    db = requests.get(settings.URL_ENV_EXPERIENCES)
    aux = db.json()
    i = 0
    for dt in aux:
        year = aux[i]['start_date']
        aux[i]['start_date'] = year[0:4]

        year = aux[i]['departure_date']
        aux[i]['departure_date'] = year[0:4]
        i = i+1

    context = {
        'dts': aux,
    }
    return render(request,'experiences.html', context)

def item_experience(request, id):
    db = requests.get(settings.URL_ENV_EXPERIENCES + id + '/')
    aux = db.json()
    acts = aux['activities'].split('\n')
    context = {
        'dts': aux,
        'acts': acts
    }
    return render(request, 'item_experience.html', context)