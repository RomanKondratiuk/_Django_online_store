from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, products, base

app_name = CatalogConfig.name

urlpatterns = [
    path('', base, name='base'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),

]

