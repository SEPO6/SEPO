# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ranking.models import Score
from django.template.loader import get_template

from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from community.models import Post_Community
from community.forms import CommunityForm, CommentForm
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def view_list(req):
	objlist = Score.objects.all()
	npage = len(objlist)/15+1
	page = req.GET.get('page')
	
	posts = []
	if page is None:
		page =1
	if page>=1 and page<=npage:
		posts = objlist.order_by('-score')[15*(page-1):15*page]

	return render(req, 'Rank.html',{'page':page, 'posts':posts})

def update_ranking():
#objlist = Score.objects.get()
	for objj in Score.objects.all():
		cnt = 0
		myscore = Score.objects.get(username = objj.username).score
		for ob in Score.objects.all():
			if ob.score > myscore:
				cnt=cnt+1
		objj.ranking = cnt+1
		objj.save()

