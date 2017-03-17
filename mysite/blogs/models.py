# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import sys
from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.

#can get chinese
reload(sys)
sys.setdefaultencoding('utf-8')

class Blog(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    mod_date = models.DateTimeField('date last modified', auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
    	return self.title
    
  