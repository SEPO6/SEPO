# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils import timezone
from ranking.models import Score
from writer.models import MyModel
from community.models import Post_Community

# Create your views here.

def mainpage(req):
    template = get_template('MainPage.html')
    context = {'rankdata' : Score.objects.order_by('-score')[:10],
			'lecdata' : MyModel.objects.order_by('id')[:10],
			'commudata' : Post_Community.objects.order_by('-id')[:10],
	}

    return HttpResponse(template.render(context))

