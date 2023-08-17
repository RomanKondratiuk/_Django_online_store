from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Имя пользователя: {name} \nEmail пользователя:{email}\nСообщение пользователя: {message}")
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/products.html', context)
