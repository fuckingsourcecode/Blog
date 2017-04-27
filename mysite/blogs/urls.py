# -*- coding: utf-8 -*-
# @Author: whistle
# @Date:   2017-01-10 19:55:27
# @Last Modified by:   fuckingsourcecode
# @Last Modified time: 2017-04-27 14:33:12
from django.conf.urls import url
# from apscheduler.schedulers.blocking import BlockingScheduler
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^articles/$', views.articles, name='articles'),
	url(r'^article/(?P<id>\d+)/$', views.article, name='article'),
	url(r'^create/$', views.create_myblog, name='create'),
	url(r'^update/(\d+)/$', views.update_myblog, name='update'),
	url(r'^delete/(\d+)/$', views.delete_myblog, name='delete'),
]
# sched = BlockingScheduler(daemonic = False)

# def mytask():
# 	print 'hello word'
# sched.add_job(mytask, 'interval', seconds=3) 
# sched.start()