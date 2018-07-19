# -*- coding: utf-8 -*-
from django import forms

from qna.models import *

class QNAForm(forms.ModelForm):
    class Meta:
        model = Post_QNA
        fields = ['title', 'whatlec', 'text']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment_QNA
		fields = ['text']
