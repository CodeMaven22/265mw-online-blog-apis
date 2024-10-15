from rest_framework import serializers
from .models import NewsArticle, CommentArticle


class CommentArticleSerializer(serializers.ModelSerializer):
    article = serializers.StringRelatedField()

    class Meta:
        model = CommentArticle
        fields = ['id', 'article', 'comment', 'date_updated', 'comment_date']


class NewsArticleSerializer(serializers.ModelSerializer):
    comments = CommentArticleSerializer(many=True, read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = NewsArticle
        fields = ['id', 'author', 'title', 'description', 'article_image', 'comments', 'date_updated', 'date_created']

    def update(self, instance, validated_data):
        # Updating the fields with the new values
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.article_image = validated_data.get('article_image', instance.article_image)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance

        # The update method is invoked automatically when a PUT or PATCH request is made to update an article.
        # This method takes two arguments:
        # instance: The current NewsArticle object you want to update.
        # validated_data: The data that was passed in and validated by the serializer.
        # In the update method, you populate the fields of the instance with either the new data from validated_data or the old values if nothing new is provided (using get('field', instance.field)).
        # Finally, you save the instance and return it.
