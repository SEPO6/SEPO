# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProblemModel(models.Model):
    title = models.CharField(max_length = 20)
    text = models.CharField(max_length = 2048)
    flag = models.CharField(max_length = 100)

