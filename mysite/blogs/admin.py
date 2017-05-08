from django.contrib import admin

from .models import Blog, BlogType, Comment
# Register your models here.

admin.site.register(Blog)
admin.site.register(BlogType)
admin.site.register(Comment)