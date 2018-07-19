
from django.conf.urls import include,url
from . import views
from community.views import *


urlpatterns = [
	url(r'^upload/',writer, name = 'community_write'),
	url(r'^edit/(?P<pk>\d+)/',edit, name = 'community_edit'),
	url(r'^delete/(?P<pk>\d+)/',delete, name = 'community_delete'),
    url(r'^view/(?P<pk>\d+)/',view_post, name = 'community_view'),
	url(r'^view/(?P<pk>\d+)/addcomment/', views.add_comment, name = 'community_addcomment'),
    url(r'^', views.view_list, name = 'community_list_view'),
]

