from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
]
=======
    path('', views.home, name='home')
]
>>>>>>> 153274383064ac882253548b68fe82f74cd1deb0
