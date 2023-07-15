from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    send_mail('Hola desde otra cuenta',
    'Hello there. Esto es un mensaje automático.',
    'sebastianalfonso2004@gmail.com',
    ['aalfonso@unsa.edu.pe'],
    fail_silently=False)

    return render(request, 'send/index.html')
    
