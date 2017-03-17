# -*- coding: utf-8 -*-
# @Author: whistle
# @Date:   2017-01-10 19:55:27
# @Last Modified by:   whistle
# @Last Modified time: 2017-03-16 14:48:52
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^(\d{4})/$', views.articles, name='articles'),
	url(r'^blog/(\d)/$', views.article, name='article'),
] 