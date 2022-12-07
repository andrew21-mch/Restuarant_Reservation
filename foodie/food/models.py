from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Menu(models.Model):
   name = models.CharField(max_length=256)
   restuarant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
   price = models.IntegerField(max_length=10)

   def __str__(self):
       return self.name

class FeedBack(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.author

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1)
    message = models.CharField(max_length=256)

    def __str__(self):
        return str(self.user)

