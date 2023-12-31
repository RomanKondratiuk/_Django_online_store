from django.shortcuts import render

from catalog.models import Product, Category


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Имя пользователя: {name} \nEmail пользователя:{email}\nСообщение пользователя: {message}")
    return render(request, 'catalog/contacts.html')


def base(request):
    products_list = Category.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Категории товаров'
    }
    return render(request, 'catalog/index.html', context)


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Все товары'
    }
    return render(request, 'catalog/products.html', context)


# def index(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Online store'
#     }
#     return render(request, 'catalog/index,html', context)