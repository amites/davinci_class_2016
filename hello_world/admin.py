from django.contrib import admin

from hello_world.models import Rating, StuffToRate


admin.site.register(Rating)
admin.site.register(StuffToRate)
