from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    new = User.objects.all()
    return HttpResponse(f'<h1> welcome yoo</h1> <h2> three amigos</h2>')

