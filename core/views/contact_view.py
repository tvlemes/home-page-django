from django.shortcuts import render, redirect
from home.settings import settings

from mailjet_rest import Client

import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from django.core.mail import EmailMessage, send_mail

def contact(request):
    return render(request, 'contacts.html')

# def contact_send_MAILJET(request):

#     email = request.POST.get('email')
#     name = request.POST.get('name')
#     phone =request.POST.get('phone')
#     subject = request.POST.get('subject')
#     message = request.POST.get('message')


#     api_key = settings.MAILJET_API_KEY
#     api_secret = settings.MAILJET_SECRET_KEY
#     mailjet = Client(auth=(api_key, api_secret), version='v3.1')

#     data = {
#     'Messages': [
#         {
#         "From": {
#             "Email": "lemes_vilarinho@yahoo.com.br",
#             "Name": "Thiago"
#         },
#         "To": [
#             {
#             "Email": "lemes_vilarinho@yahoo.com.br",
#             "Name": "Thiago"
#             }
#         ],
#         "Subject": 'subject',
#         "TextPart": 'message',
#         "HTMLPart": "<h3>Envio de email</h3>",
#         "CustomID": "AppGettingStartedTest"
#         }
#     ]
#     }
#     result = mailjet.send.create(data=data)
#     print(result.status_code)
#     print (result.json())
  
    
#     return redirect('/contacts/')

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
