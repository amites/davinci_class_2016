from django.conf.urls import url

from hello_world.views import hello_name, index


urlpatterns = [
    url(r'^hello$', hello_name, name='hello'),
    url(r'^$', index, name='index'),
]
