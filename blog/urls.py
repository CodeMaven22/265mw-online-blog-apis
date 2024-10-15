from django.urls import path
from .views import NewsArticleCreateAPIView,  NewsArticleListAPIView, \
    NewsArticleDetailAPIView, NewsArticleAgricultureListAPIView, NewsArticleSportsListAPIView, \
    NewsArticleEducationListAPIView, NewsArticleTechnologyListAPIView, NewsArticleHealthListAPIView, \
    CommentArticleCreateAPIView, CommentArticleDetailAPIView, \
    CommentArticleListAPIView, NewsArticleListCreateAPIView

urlpatterns = [
    path('create-article/', NewsArticleCreateAPIView.as_view(), name='create-article'),
    path('create-list-article/', NewsArticleListCreateAPIView.as_view(), name='create-list'),
    path('article-list/', NewsArticleListAPIView.as_view(), name='articles-list'),
    path('article-detail/<int:pk>/', NewsArticleDetailAPIView.as_view(), name='article-detail'),
    path('article-sports/', NewsArticleSportsListAPIView.as_view(), name='article-sports'),
    path('article-education/', NewsArticleEducationListAPIView.as_view(), name='article-education'),
    path('article-technology/', NewsArticleTechnologyListAPIView.as_view(), name='article-technology'),
    path('article-agriculture/', NewsArticleAgricultureListAPIView.as_view(), name='article-agriculture'),
    path('article-health/', NewsArticleHealthListAPIView.as_view(), name='article-health'),
    path('create-comment/<int:article_id>/', CommentArticleCreateAPIView.as_view(), name='article-comments'),
    path('comments-list/', CommentArticleListAPIView.as_view(), name='comments-list'),
    path('comments-detail/int:pk/', CommentArticleDetailAPIView.as_view(), name='comment-details')

]
