#from django.urls import path
from django.conf.urls import include,url
from user_manager.views import login,login_validate, join
from . import views


urlpatterns = [
	url(r'^/',login),
	url(r'^login/$',login),
	url(r'^login/validate/$',login_validate),
	url(r'^join/$',join),
]

