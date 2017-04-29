from django.contrib import admin

from .models import Blog, BlogType
# Register your models here.

admin.site.register(Blog)
admin.site.register(BlogType)