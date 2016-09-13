from django.conf.urls import url

from hello_world.views import hello_name, index


urlpatterns = [
    url(r'^hello$', hello_name),
    url(r'^$', index),
]
