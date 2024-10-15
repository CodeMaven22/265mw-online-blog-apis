from django.contrib import admin
from .models import NewsArticle, CommentArticle

# Register your models here.
admin.site.register(NewsArticle)
admin.site.register(CommentArticle)
