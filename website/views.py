from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import *
from .functions import *
import json

# Template Views
def index(request):
    data = {}
    data['products'] = Product.objects.all()
    return render(request, 'website/index.html', data)

def contact(request):
    data = {}
    if request.POST.get("comentario") and request.POST.get("email"):
        nombreF = request.POST.get("nombre")
        emailF = request.POST.get("email")
        comentarioF = request.POST.get("comentario")

        asunto = nombreF + ' se ha comunicado '
        mensaje = comentarioF + '\n' + 'Favor de responder a: ' + emailF
        sendMailContact(asunto, 'pasteleria.gorey2021@gmail.com', mensaje)
        return redirect(to='index')
    return render(request, 'website/contact.html', data)

def resume(request, id_buy):
    data = {}
    buy = Buy.objects.get(id_buy = id_buy)
    data['buy'] = buy
    data['client'] = buy.id_client
    data['buyItems'] = ItemsBuy.objects.filter(id_buy = buy)

    return render(request, 'website/resume.html', data)

def payment(request, id_buy):
    data = {}

    buy = Buy.objects.get(id_buy = id_buy)
    buy.isPaid = True
    buy.save()

    client = buy.id_client

    items = ItemsBuy.objects.filter(id_buy = buy)
    message = 'Productos adquiridos: <br><br>'
    for i in items:
        message += str(i.id_product.name) + ' - ' +  str(i.quantity) + ' piezas ( $' + "{:.2f}".format(i.id_product.price) + ' c/u ) <br>'

    message += '<br><br>Total pagado: ' + str(buy.total) + ' <br>No. de pedido: ' + str(buy.id_buy) + '<br>'
    message += '<br>Gracias por comprar con nosotros'

    sendMail('Resumen de pedido', client.email, message)

    return redirect(to='thanks')

def thanks(request):
    data = {}
    return render(request, 'website/thanks.html', data)

def tickets(request):
    data = {}
    if not request.user.is_superuser:
        return redirect(to='index')
    
    buys = Buy.objects.all()
    data['buys'] = buys

    return render(request, 'website/tickets.html', data)

# API Views

def api_load_buy(request, id_buy):
    data = {}

    buy = Buy.objects.get(id_buy = id_buy)
    items = ItemsBuy.objects.filter(id_buy = buy)
    listItems = list()
    for i in items:
        listItems.append({'name': i.id_product.name, 'quantity': i.quantity, 'price': i.id_product.price } )
    data['buyItems'] = listItems

    return JsonResponse(data)

def api_load_cart(request):
    data = {}
    # Get the POST vars
    cart = json.loads(str(request.POST.get('cart')))
    total = request.POST.get('total')
    name = request.POST.get('name')
    email = request.POST.get('email')

    if Client.objects.filter(email = email).exists():
        # Get the client
        client = Client.objects.get(email = email)
    else:
        # Create the client
        client = Client.objects.create(name = name, email = email)
        client.save()

    # Create the buy
    buy = Buy.objects.create(total = total, isPaid = False, id_client = client)
    buy.save()

    # Add the products to Items-Buy
    for i in cart:
        product = Product.objects.get(id_product = i['id_product'])
        itemBuy = ItemsBuy.objects.create(id_buy = buy, id_product = product, quantity = i['quantity'])
        itemBuy.save()

    data['IDBuy'] = buy.id_buy
    data['message'] = 'OK'

    return JsonResponse(data)

def api_set_delivered(request, id_buy):
    buy = Buy.objects.get(id_buy = id_buy)
    buy.isDelivered = True
    buy.save()

    return redirect(to='tickets')