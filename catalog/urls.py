from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductsListView, CategoryListView, BlogpostCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='base'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('create/', BlogpostCreateView.as_view(), name='create'),

]

