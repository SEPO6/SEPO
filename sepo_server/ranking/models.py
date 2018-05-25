# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Score(models.Model):
    username = models.CharField(max_length = 30)
    score = models.IntegerField(default = 0)

class SolvedList(models.Model):
    username = models.CharField(max_length = 30)
    pnum = models.IntegerField(default = 0)


