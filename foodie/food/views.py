from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Menu


def home(request):
    new = User.objects.all()
    return HttpResponse(f'<h1> welcome yoo</h1> <h2> three amigos</h2>')

def food(request):
    return render(request, 'food.html')

def resto(request):
    return render(request, 'resto.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def signup_client(request):
    return render(request, 'signup_client.html')

def signup_resto(request):
    return render(request, 'signup_resto.html')

def resto_client(request):
    return render(request, 'resto_client.html')

def client_food(request):
    return render(request, 'client_food.html')

def menu(request):
    return render(request, 'menu.html')

def table(request):
    return render(request, 'table.html')

def confirm_table(request):
    return render(request, 'confirm_table.html')

def confirm_menu(request):
    return render(request, 'confirm_menu.html')

def resto_dashboard(request):
    return render(request, 'resto_dashboard.html')

def resto_menu(request):
    return render(request, 'resto_menu.html')

def resto_table(request):
    return render(request, 'resto_table.html')

def create_menu(request):
    return render(request, 'create_menu.html')

def create_table(request):
    return render(request, 'create_table.html')

def landing_page(request):
    return render(request, 'landing_page.html')

# Create your views here.

def index(request):
    if request.method == 'POST':
        query = request.POST['query']

        if Menu.objects.filter(name=query).exists():
            searches = Menu.objects.filter(name=query)
            return render(request, 'index.html', {'searches':searches})

        else:
            messages.info(request, 'Oops Be like the no cook your food today oh! try another favourite')
            return redirect('index')
    else:
        return render(request, 'index.html')
