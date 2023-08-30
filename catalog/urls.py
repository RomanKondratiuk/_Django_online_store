from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductsListView, CategoryListView, ProductCreateView, \
    ProductUpdateView, ProductDetailView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='base'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('<int:pk>', ProductDetailView.as_view(), name='view_product'),

    path('create/', ProductCreateView.as_view(), name='create_products'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),

    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_products'),


]

