from django.contrib import admin

from hello_world.models import Order, Pet, Rating, StuffToRate, Customer


admin.site.register(Rating)
admin.site.register(StuffToRate)

admin.site.register(Pet)

admin.site.register(Customer)
admin.site.register(Order)
