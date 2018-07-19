
from django.conf.urls import include,url
from . import views
from qna.views import *


urlpatterns = [
	url(r'^upload/',writer),
	url(r'^edit/(?P<pk>\d+)/',edit, name = 'qna_edit'),
	url(r'^delete/(?P<pk>\d+)/',delete, name = 'qna_delete'),
	url(r'^view/(?P<pk>\d+)/',view_post, name = 'qna_view'),
	url(r'^view/(?P<pk>\d+)/addcomment/', views.add_comment, name = 'qna_addcomment'),
    url(r'^', views.view_list, name = 'qna_list_view'),
]

