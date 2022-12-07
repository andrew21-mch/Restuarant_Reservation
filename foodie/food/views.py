from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

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