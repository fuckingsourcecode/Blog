# -*- coding: utf-8 -*-
# @Author: whistle
# @Date:   2017-01-10 19:55:36
# @Last Modified by:   fuckingsourcecode
# @Last Modified time: 2017-05-06 14:20:47
from django.conf.urls import url
import views
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
urlpatterns = [
	url(r'^$', views.login, name = 'login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^changepassword/$', views.changepassword, name='changepassword'),
	url(r'^blog/$', views.blog, name='blog'),
	url(r'^information/$', views.information, name='information'),
	url(r'^query/$', views.query, name='query'),
	url(r'^queryemail/$', views.queryemail, name='queryemail'),
	url(r'^account/(?P<id>\w+)/$', views.account, name='account'),
	url(r'^getfictionblog/$', views.getfictionblog, name='getfictionblog'),
] 