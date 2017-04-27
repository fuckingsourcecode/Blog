# -*- coding: utf-8 -*-
# @Author: whistle
# @Date:   2017-01-10 19:55:36
# @Last Modified by:   fuckingsourcecode
# @Last Modified time: 2017-04-27 14:33:05
from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^changepassword/$', views.changepassword, name='changepassword'),
	url(r'^blog/$', views.blog, name='blog'),
] 