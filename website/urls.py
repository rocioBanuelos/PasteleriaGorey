from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('resume/<int:id_buy>', views.resume, name="resume"),
    path('payment/<int:id_buy>', views.payment, name="payment"),
    path('thanks', views.thanks, name="thanks"),
    path('tickets', views.tickets, name="tickets"),

    path('api/loadBuy/<int:id_buy>', views.api_load_buy, name='loadBuy'),
    path('api/loadShopCart', views.api_load_cart, name='apiLoadCart'),
    path('api/setDelivered/<int:id_buy>', views.api_set_delivered, name='setDelivered'),
]