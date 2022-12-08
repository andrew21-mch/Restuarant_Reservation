from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Menu


# Views goes here

def home(request):
    new = User.objects.all()
    return HttpResponse(f'<h1> welcome yoo</h1> <h2> three amigos</h2>')

def food(request):
    return render(request, 'food.html')

def resto(request):
    return render(request, 'resto.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_staff == True:
                return redirect('resto_dashboard')
            else:
                return redirect('resto_client')

        else:
            messages.info(request, "wrong credentials please try again")
            return redirect('login')

    else:

        return render(request, 'login.html')

def signup(request):

    return render(request, 'signup.html')

def signup_client(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('signup_client')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('signup_client')

            else:
                user = User.objects.create_user(username=username, password=password1, first_name=phone, email=email, is_staff=False)
                user.save()
                return redirect('login')
        else:

            messages.info(request, 'password mismatched') # message if there is password mismatched
            return redirect('signup_client')
    else:
        return render(request, 'signup_client.html')

def signup_resto(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        location = request.POST['location']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'restuarent already exist')
                return redirect('signup_resto')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist') # gives an error if email already exist
                return redirect('signup_resto')

            else:
                user = User.objects.create_user(username=username, password=password1, first_name=phone, last_name=location, email=email, is_staff=True)
                user.save()
                return redirect('login')
        else:

            messages.info(request, 'password mismatched')
            return redirect('signup_resto')
    else:
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
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')

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
    
