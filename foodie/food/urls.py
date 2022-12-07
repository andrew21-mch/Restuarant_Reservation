from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('food', views.food, name='food'),
    path('resto', views.resto, name='resto'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signup_client', views.signup_client, name='signup_client'),
    path('signup_resto', views.signup_resto, name='signup_resto'),




    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]