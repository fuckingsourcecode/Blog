# -*- coding: utf-8 -*-
# @Author: whistle
# @Date:   2017-01-10 19:55:27
# @Last Modified by:   fuckingsourcecode
# @Last Modified time: 2017-04-29 15:56:16
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.articles, name = 'index'),
	url(r'^articles/$', views.articles, name='articles'),
	url(r'^article/(?P<id>\d+)/$', views.article, name='article'),
	url(r'^create/$', views.create_myblog, name='create'),
	url(r'^update/(\d+)/$', views.update_myblog, name='update'),
	url(r'^delete/(\d+)/$', views.delete_myblog, name='delete'),
	url(r'^blog/(?P<id>\d+)/$', views.article, name='article'),
	url(r'^fiction/(?P<id>\d+)/$', views.fiction, name='fiction'),
	url(r'^good/(?P<id>\d+)/$', views.good, name='good'),
	url(r'^create_comment/(?P<id>\d+)/$', views.create_comment, name='create_comment'),
	# url(r'^publish/(?P<id>\d+)/(?P<status>)/$', views.publish_myblog, name='publish'),
]
