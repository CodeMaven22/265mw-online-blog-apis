from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import get_object_or_404
from .serializers import NewsArticleSerializer, CommentArticleSerializer
from .models import NewsArticle, CommentArticle


# Create your views here.
class NewsArticleCreateAPIView(generics.CreateAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the author field to the currently authenticated user
        # Ensure the user is logged in for this to work, otherwise adjust accordingly
        serializer.save(author=self.request.user)


class NewsArticleListCreateAPIView(generics.ListCreateAPIView):
    # queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Set the author field to the currently authenticated user
        # Ensure the user is logged in for this to work, otherwise adjust accordingly
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return NewsArticle.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"Message": "No articles available", "Articles": []}, status=status.HTTP_200_OK)
        return super().get(request, *args, **kwargs)


class NewsArticleListAPIView(generics.ListAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    permission_classes = [AllowAny]


class NewsArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NewsArticleSportsListAPIView(generics.ListAPIView):
    serializer_class = NewsArticleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return NewsArticle.objects.filter(category='sports')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No articles available", "articles": []}, status=status.HTTP_200_OK)
        return super().get(request, *args, **kwargs)


class NewsArticleEducationListAPIView(generics.ListAPIView):
    queryset = NewsArticle.objects.filter(category='education')
    serializer_class = NewsArticleSerializer
    permission_classes = [AllowAny]


class NewsArticleTechnologyListAPIView(generics.ListAPIView):
    serializer_class = NewsArticleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return NewsArticle.objects.filter(category='technology')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No articles available", "articles": []}, status=status.HTTP_200_OK)
        return super().get(request, *args, **kwargs)


class NewsArticleAgricultureListAPIView(generics.ListAPIView):
    serializer_class = NewsArticleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return NewsArticle.objects.filter(category='agriculture')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No articles available", "articles": []}, status=status.HTTP_200_OK)
        return super().get(request, *args, **kwargs)


class NewsArticleHealthListAPIView(generics.ListAPIView):
    serializer_class = NewsArticleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return NewsArticle.objects.filter(category='health')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No articles available", "articles": []}, status=status.HTTP_200_OK)
        return super().get(request, *args, **kwargs)


class CommentArticleCreateAPIView(generics.CreateAPIView):
    queryset = CommentArticle.objects.all()
    serializer_class = CommentArticleSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        article_pk = self.kwargs.get('article_id')  # Get the article primary key from URL
        article = get_object_or_404(NewsArticle,
                                    pk=article_pk)  # Fetch the News Article object or return 404 if not found
        serializer.save(article=article)  # Save the review with the ebook instance


class CommentArticleListAPIView(generics.ListAPIView):
    queryset = CommentArticle.objects.all()
    serializer_class = CommentArticleSerializer
    permission_classes = [AllowAny]


class CommentArticleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentArticle.objects.all()
    serializer_class = CommentArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
