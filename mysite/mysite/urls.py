"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views
# from apscheduler.schedulers.blocking import BlockingScheduler
from blogs.views import *
admin.autodiscover()
urlpatterns = [
    url(r'^$', articles),
    url(r'^admin/', admin.site.urls),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^message/', include('message.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] +  static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )



# sched = BlockingScheduler(daemonic = False)

# def mytask():
#   print 'hello word'
# sched.add_job(mytask, 'interval', seconds=3) 
# sched.start()