from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

from .models import Bookings, Menu, Restaurant


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
                messages.info(request, 'username already exist')
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
# start untested code
# ==================================

def add_resto(request):
    if request.method == 'POST':
        ownerId = request.user
        print(ownerId)
        name = request.POST['name']
        location = request.POST['location']

        if Restaurant.objects.filter(name=name).exists():
            messages.info(request, 'restuarent already exist')
            return redirect('create_resto')
        else:
            resto = Restaurant(owner=ownerId, name=name, location=location)
            resto.save()
            return redirect('resto_dashboard')
    else:
        return render(request, 'create_resto.html')



def add_menu(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']

        if Menu.objects.filter(name=name).exists():
            messages.info(request, 'menu already exist')
            return redirect('add_menu')
        else:
            menu = Menu(name=name, price=price, description=description, image=image)
            menu.save()
            return redirect('resto_menu')
    else:
        return render(request, 'add_menu.html')

def view_orders(request):
    resto = Restaurant.objects.filter(ownerId=request.user.id).exists()
    if resto:
        orders = Bookings.objects.filter(restoId=resto.id)
        return render(request, 'view_orders.html', {'orders': orders})
    else:
        return redirect('resto_dashboard')

# ==================================
# end untested


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

@login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff, login_url='resto_client')
def resto_dashboard(request):
    user_resto = Restaurant.objects.get(owner=request.user)
    return render(request, 'resto_dashboard.html', {'user_resto': user_resto})

def resto_menu(request):
    return render(request, 'resto_menu.html')

def resto_table(request):
    return render(request, 'resto_table.html')

@login_required(login_url='login')
def create_menu(request):
    return render(request, 'create_menu.html')

@login_required(login_url='login')
def create_table(request):
    return render(request, 'create_table.html')

def landing_page(request):
    return render(request, 'landing_page.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def search_food(request):
    query = request.GET.get('query')
    if(Menu.objects.filter(name__icontains=query).exists()):
        food = Menu.objects.filter(name__icontains=query)
        return render(request, 'client_food.html', {'food': food})
    else:
        messages.info(request, 'Ooops, Sorry we dont have that food today, try another favourite')
        return redirect('client_food')
def search_resto(request):
    query = request.GET.get('query')
    if(query == '' or query == None):
        restos = Restaurant.objects.all()
        return render(request, 'resto_client.html', {'restos': restos})
    if(Restaurant.objects.filter(name__icontains=query).exists() or Restaurant.objects.filter(location__icontains=query).exists()):
        resto = Restaurant.objects.filter(name__icontains=query)
        return render(request, 'resto_client.html', {'restos': resto})
    else:
        messages.info(request, 'Ooops, Sorry we dont have that restaurant today, try another favourite')
        return redirect('resto_client')
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

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('index')
