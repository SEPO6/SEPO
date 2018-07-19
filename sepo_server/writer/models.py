# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Create your models here.

class MyModel(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = RichTextUploadingField()
	published_date = models.DateTimeField(blank = True , null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
