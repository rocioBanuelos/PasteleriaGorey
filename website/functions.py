from .models import *
from django.core.mail import send_mail

def sendMail(subject, destiny, message):
    send_mail(
        'Pasteles Gorey: ' + subject,
        message,
        'Resumen de pedido',
        [destiny],
        html_message = message
    )
    return True

def sendMailContact(subject, destiny, message):
    send_mail(
        'Contacto Pastelería Gorey: ' + subject,
        message,
        'Pastelería Gorey Contacto',
        [destiny],
        html_message = message
    )
    return True