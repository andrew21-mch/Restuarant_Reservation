from django.contrib import admin
from .models import Menu, Restaurant, Bookings, FeedBack

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Bookings)
admin.site.register(FeedBack)
