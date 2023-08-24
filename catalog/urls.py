from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, category_product, ProductsListView, CategoryListView, BlogpostCreateView, BlogpostUpdateView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='base'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    # path('<int:pk>/products', category_product, name='category_product'),
    path('<int:pk>', ProductDetailView.as_view(), name='view_product'),
    path('create/', BlogpostCreateView.as_view(), name='create_products'),
    path('edit/<int:pk>/', BlogpostUpdateView.as_view(), name='update_products'),

]

