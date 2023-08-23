from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from catalog.models import Product, Category, BlogPost


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Имя пользователя: {name} \nEmail пользователя:{email}\nСообщение пользователя: {message}")
    return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/index.html'


class ProductsListView(ListView):
    model = Product
    template_name = 'catalog/products.html'


class BlogpostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'slug', 'content', 'image', 'date_of_creation', 'sign_publication', 'number_of_views',)
    # fields = ('title',)
    success_url = reverse_lazy('catalog:products')
