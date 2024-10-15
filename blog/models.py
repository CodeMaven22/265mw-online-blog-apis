from django.db import models
from useraccount.models import CustomUser


class NewsArticle(models.Model):
    ARTICLE_CATEGORY = [
        ('sports', 'Sports'),
        ('agriculture', 'Agriculture'),
        ('technology', 'Technology'),
        ('health', 'Health'),
        ('education', 'Education')
    ]

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=155)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=ARTICLE_CATEGORY, default='', null=True, blank=True)
    article_image = models.ImageField(blank=True, null=True, upload_to='articles_image/')
    like_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(CustomUser, related_name='liked_articles', blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_created = models.DateField()

    def __str__(self):
        return self.title


class CommentArticle(models.Model):
    article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    date_updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
