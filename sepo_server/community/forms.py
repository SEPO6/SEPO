# -*- coding: utf-8 -*-
from django import forms

from community.models import Post_Community, Comment_Community

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Post_Community
        fields = ['title', 'text']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment_Community
		fields = ['text']
