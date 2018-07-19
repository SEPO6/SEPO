# -*- coding: utf-8 -*-
from django import forms

from writer.models import MyModel

class PostForm(forms.ModelForm):
	class Meta:
		model = MyModel
		fields = ['title','text']
