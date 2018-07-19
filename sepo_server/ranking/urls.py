
from django.conf.urls import include,url
from . import views
from ranking.views import *


urlpatterns = [

    url(r'^', view_list, name = 'ranking_list_view'),
]

