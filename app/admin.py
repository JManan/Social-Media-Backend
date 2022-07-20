from django.contrib import admin
# Register your models here.

from .models import PostList, Comment

admin.site.register(PostList)
admin.site.register(Comment)
