from django.shortcuts import render, redirect
from home.settings import settings

def contact(request):
    return render(request, 'contacts.html')

