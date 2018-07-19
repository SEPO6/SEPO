# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from problem.models import ProblemModel
from problem.forms import PostForm
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import redirect
from ranking.models import Score, SolvedList
from writer.urls import *
from ranking.views import update_ranking
# Create your views here.

def post_problem(req,pk):
    post = get_object_or_404(ProblemModel, pk = pk)
    
    solved = "Not Solved"
    if len(SolvedList.objects.filter(username = req.user, pnum=pk)) is not 0:
		solved = "Solved"

    return render(req, 'Problem.html', {'post' : post, 'answerform': PostForm(), 'solved' : solved})

def prob_validate(req,pk):
    answer = PostForm(req.POST)
    post = get_object_or_404(ProblemModel,pk=pk)

    if answer.is_valid():
        #return HttpResponse(answer.cleaned_data['fl'])
        #return HttpResponse(ProblemModel.objects.get(id = int(pk)).flag)
        if answer.cleaned_data['fl'] == ProblemModel.objects.get(id = int(pk)).flag:
            row = Score.objects.get(username=req.user)
            if len(SolvedList.objects.filter(username = req.user, pnum=pk)) is 0 :
                row.score = row.score + 5
                row.save()
                SolvedList.objects.create(username = req.user, pnum = pk)
                update_ranking()
            	return redirect('/')
        else:
            return HttpResponse('Answer is wrong!')
    else:
        return HttpResponse('Abnormal Form!')




