from django.urls import path
from . import views


# patterns to view on the browser
urlpatterns = [
    path('food', views.food, name='food'),
    path('resto', views.resto, name='resto'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('signup_client', views.signup_client, name='signup_client'),
    path('signup_resto', views.signup_resto, name='signup_resto'),
    path('add_resto', views.add_resto, name='add_resto'),
    path('resto_client', views.resto_client, name='resto_client'),
    path('client_food', views.client_food, name='client_food'),
    path('search_food', views.search_food, name='search_food'),
    path('search_resto', views.search_resto, name='search_resto'),
    path('menu', views.menu, name='menu'),
    path('table', views.table, name='table'),
    path('confirm_table', views.confirm_table, name='confirm_table'),
    path('confirm_menu', views.confirm_menu, name='confirm_menu'),
    path('resto_dashboard', views.resto_dashboard, name='resto_dashboard'),
    path('resto_table', views.resto_table, name='resto_table'),
    path('resto_menu', views.resto_menu, name='resto_menu'),
    path('create_menu', views.create_menu, name='create_menu'),
    path('create_table', views.create_table, name='create_table'),
    path('contact', views.contact, name='contact'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
