from django.urls import path

from catalog.views import contacts, products, base

urlpatterns = [
    path('', base, name='base'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),

]

