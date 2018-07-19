#from django.urls import path
from django.conf.urls import include,url
from user_manager.views import login,login_validate, join
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^logout/$', auth_views.logout, {'next_page' : '/'}),
	url(r'^login/$',login),
	url(r'^login/validate/$',login_validate),
	url(r'^join/$',join),
]

