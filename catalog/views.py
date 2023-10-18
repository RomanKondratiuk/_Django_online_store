from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.contrib.auth.decorators import login_required


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

    def get_queryset(self):
        # Фильтруем продукты так, чтобы возвращались только те, у которых владельцем является текущий пользователь
        return Product.objects.filter(owner=self.request.user)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/view_product.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')
