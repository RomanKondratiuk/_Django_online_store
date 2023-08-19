from django.urls import path

from catalog.views import contacts, products, base

urlpatterns = [
    path('', base),
    path('contacts/', contacts),
    path('products/', products),

]

