from __future__ import unicode_literals
import sys
from django.conf import settings
from django.db import models
from django import forms
from django.contrib.auth.admin import UserAdmin
import datetime
# Create your models here.
reload(sys)
sys.setdefaultencoding('utf-8')

# class User(models.Model):
#     """
#     Description: Model Description
#     	User Information
#     	gender: true->male false->female
#     """
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)
#     mobile = models.CharField(max_length=11, unique=True)
#     occupation = models.CharField(max_length=100, default="none")
#     address = models.CharField(max_length=100, default="none")
#     url = models.URLField(max_length=200)
#     last_login = models.CharField(max_length=50)
#     def __str__(self):
#         return self.email
    # class Meta: