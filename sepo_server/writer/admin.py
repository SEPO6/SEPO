# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from writer.models import MyModel

# Register your models here.

admin.site.register(MyModel)
