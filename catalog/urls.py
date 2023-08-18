from django.urls import path, include

from catalog.views import contacts, products, home

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products),

]

