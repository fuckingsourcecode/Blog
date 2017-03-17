# -*- coding: utf-8 -*-
# @Author: whistle
# @Date:   2017-01-10 19:55:36
# @Last Modified by:   whistle
# @Last Modified time: 2017-03-16 14:39:53
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.login, name='login'),
	# url(r'^login/$', auth_views.login, name='login'),
	# url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^forgetpassword/$', views.forgetpassword, name='forgetpassword'),
	url(r'^(\d)/$', views.user, name='user'),
] 