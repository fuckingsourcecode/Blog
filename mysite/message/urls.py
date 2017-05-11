# -*- coding: utf-8 -*-
# @Author: fuckingsourcecode
# @Date:   2017-05-11 14:11:49
# @Last Modified by:   fuckingsourcecode
# @Last Modified time: 2017-05-11 19:28:35
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.create_message, name = 'create_message'),
]