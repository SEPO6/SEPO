# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from community.models import Post_Community
from community.forms import CommunityForm, CommentForm
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def writer(req):
	if req.method == "POST":
		form = CommunityForm(req.POST)
		if form.is_valid():
			post_item = form.save(commit=False)
			post_item.author = req.user
			post_item.published_date =  timezone.now()
			post_item.save()
			return redirect('/community/')
	else:
		form = CommunityForm()

	return render(req, 'posting.html', {'form':form})

def edit(req,pk):
	post = get_object_or_404(Post_Community, pk = pk)
	if req.method =="POST":
		form=CommunityForm(req.POST, instance = post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author = req.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/community/view/', pk = post.pk)
	else:
		form = CommunityForm(instance = post)		
	return render(req, 'posting.html', {'form':form})

def delete(req,pk):
	post = get_object_or_404(Post_Community, pk=pk)
	post.delete()
	return redirect('/community/')

def view_post(req, pk):
	post = get_object_or_404(Post_Community, pk=pk)
	return render(req, 'postpage.html',{'post':post})

def add_comment(req,pk):
	post = get_object_or_404(Post_Community, pk=pk)
	if req.method == "POST":
		form = CommentForm(req.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post=post
			comment.save()
			return redirect('/community/view/', pk = post.pk)
	else:
		form = CommentForm()
	return render(req, 'addcomment.html', {'form':form})

def view_list(req):
	objlist = Post_Community.objects.all()
	paginator = Paginator(objlist,15)
	page = req.GET.get('page')
	
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(req, 'community.html',{'page':page, 'posts':posts})

