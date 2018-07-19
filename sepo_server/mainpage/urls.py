#from django.urls import path
from django.conf.urls import include,url
from mainpage.views import mainpage

urlpatterns = [
	url('',mainpage, name = 'mainpage'),
]

