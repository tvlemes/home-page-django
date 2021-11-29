from django.shortcuts import render, redirect
from home.settings import settings

def dashboard(request):
    return redirect(settings.URL_ENV_DASHBOARD)