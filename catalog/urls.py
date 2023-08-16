from django.urls import path, include

from catalog.views import contacts, home, products

urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products)

]

