from django.contrib import admin
from .models import News, Tag
from comments.models import Comment


admin.site.register(News)
admin.site.register(Tag)
admin.site.register(Comment)