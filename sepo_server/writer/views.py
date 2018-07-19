# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Context
from django.template.loader import get_template

from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from writer.models import MyModel
from writer.forms import PostForm
from django.utils import timezone

# Create your views here.

def test_writer(req):
	if req.method == "POST":
		form = PostForm(req.POST)
		if form.is_valid():
			post_item = form.save(commit=False)
			post_item.author = req.user
			post_item.published_date =  timezone.now()
			post_item.save()
			return redirect('/community/')
	else:
		form = PostForm()

	return render(req, 'posting.html', {'form':form})

def edit(req,pk):
	post = get_object_or_404(MyModel, pk = pk)
	if req.method =="POST":
		form=PostForm(req.POST, instance = post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author = req.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/community/')
	else:
		form = PostForm(instance = post)		
	return render(req, 'posting.html', {'form':form})

def delete(req,pk):
	post = get_object_or_404(MyModel, pk=pk)
	post.delete()
	return redirect('/community/')

def view(req, pk):
	post = get_object_or_404(MyModel, pk=pk)
	plist = MyModel.objects.order_by('id')[:]
	st = int(pk)-5
	en = int(pk)+5
	if st<0 :
		st=0
		en=10
	elif en > len(plist) :
		st = len(plist)-10		
		en = len(plist)	
	
	plink = {'1':'1', '2':'3', '3':'4', '4':'4', '5':'5', '6':'5', '7':'6', '8':'6', '9':'6', '10':'7', '11':'7', '12':'8', }

	context = {'lecdata' : MyModel.objects.order_by('id')[st:en], 'post':post, 'plink':plink[pk]}
	return render(req, 'Lecture1.html',context)

    


    
