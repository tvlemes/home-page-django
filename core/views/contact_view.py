from django.shortcuts import render, redirect
from home.settings import settings

from mailjet_rest import Client

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.core.mail import EmailMessage, send_mail

def contact(request):
    return render(request, 'contacts.html')

def contact_send(request):
    status = send_mail(
        "Assunto do email Anymail", # Assunto
        "Texto", # Mensagem
        'contatothiagolemes@gmail.com', # Remetente
        ["lemes_vilarinho@yahoo.com.br"], # Destinatário
        settings.API_KEY_SENDINBLUE,
        html_message="<html>Email pelo Anymail</html>",
        )
    print(status)
    
    return redirect('/contacts/')
