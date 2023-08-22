from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductsListView, CategoryListView  # products, base, ProductsListView


app_name = CatalogConfig.name

urlpatterns = [
    # path('', base, name='base'),
    path('', CategoryListView.as_view(), name='base'),
    path('contacts/', contacts, name='contacts'),
    # path('products/', products, name='products'),
    path('products/', ProductsListView.as_view(), name='products'),

]

