from django.conf.urls import url
from base import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^play', views.register, name='start'),
	url(r'^game', views.game, name='game'),
]
