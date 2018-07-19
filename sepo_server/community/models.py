# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post_Community(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField(default = ' ')
    published_date = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.title

class Comment_Community(models.Model):
	post = models.ForeignKey('community.Post_Community', related_name = 'comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(blank = True, null = True)

	def __str__(self):
		return self.title

	
