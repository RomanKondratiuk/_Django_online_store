from django.shortcuts import render


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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Имя пользователя: {name} \nEmail пользователя:{email}\nСообщение пользователя: {message}")
    return render(request, 'catalog/products.html')
