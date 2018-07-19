# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from qna.models import *
from qna.forms import *
from django.utils import timezone

# Create your views here.

def writer(req):
	if req.method == "POST":
		form = QNAForm(req.POST)
		if form.is_valid():
			post_item = form.save(commit=False)
			post_item.author = req.user
			post_item.published_date =  timezone.now()
			post_item.save()
			return redirect('/qna/')
	else:
		form = QNAForm()

	return render(req, 'posting.html', {'form':form})

def edit(req,pk):
	post = get_object_or_404(Post_QNA, pk = pk)
	if req.method =="POST":
		form=QNAForm(req.POST, instance = post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author = req.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/qna/')
	else:
		form = QNAForm(instance = post)		
	return render(req, 'posting.html', {'form':form})

def delete(req,pk):
	post = get_object_or_404(Post_QNA, pk=pk)
	post.delete()
	return redirect('/qna/')

def view_post(req, pk):
	post = get_object_or_404(Post_QNA, pk=pk)
	return render(req, 'qna_post.html',{'post':post})

def add_comment(req,pk):
	post = get_object_or_404(Post_QNA, pk=pk)
	if req.method == "POST":
		form = CommentForm(req.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post=post
			comment.save()
			return redirect('/qna/view/', pk = post.pk)
	else:
		form = CommentForm()
	return render(req, 'addcomment.html', {'form':form})

def view_list(req):
	objlist = Post_QNA.objects.all()
	paginator = Paginator(objlist,15)
	page = req.GET.get('page')
	
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(req, 'qna.html',{'page':page, 'posts':posts})






