from django.conf.urls import include, url
from problem.views import *

urlpatterns = [
	url(r'^(?P<pk>\d+)/$', post_problem ,name = 'post_problem'),
	url(r'^(?P<pk>\d+)/validate/$', prob_validate, name = 'prob_validate'),
]
