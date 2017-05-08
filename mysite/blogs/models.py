# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import sys
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
# Create your models here.

#can get chinese
reload(sys)
sys.setdefaultencoding('utf-8')

class BlogType(models.Model):
    blog_type = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.blog_type
        
class Blog(models.Model):
    """
    Description: Model Description
    """
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    mod_date = models.DateTimeField('date last modified', auto_now = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    summary = models.CharField(max_length=600)
    hot = models.IntegerField(default=0)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    def __str__(self):
    	return self.title
class Comment(models.Model):
    pub_date = models.DateTimeField('date published', default=timezone.now)
    comment = models.CharField(max_length=300)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment

