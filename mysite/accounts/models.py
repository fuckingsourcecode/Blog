from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django import forms
from django.contrib.auth.admin import UserAdmin
import datetime
# Create your models here.

class User(models.Model):
    """
    Description: Model Description
    	User Information
    	gender: true->male false->female
    """
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=11, unique=True)
    last_login = models.CharField(max_length=50)
    def __str__(self):
        return self.email
    # class Meta: