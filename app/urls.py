from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('',views.index,name='home'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('cart',views.cart,name='cart'),
    path('icecream',views.icecream,name='icecream'),
    path('cake',views.cake,name='cake'),
    path('pastries',views.pastries,name='pastries'),
 path('waffles',views.waffles,name='waffles'),
 path('donuts',views.donuts,name='donuts'),
 path('checkout',views.checkout,name='checkout')

]
