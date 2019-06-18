from django.conf.urls import url
from Apps.Administrador.views import *
urlpatterns = [
    url(r'^$', index, name='index')
	]