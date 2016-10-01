from django.contrib import admin

from hello_world.models import Pet, Rating, StuffToRate


admin.site.register(Rating)
admin.site.register(StuffToRate)

admin.site.register(Pet)
