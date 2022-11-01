from rest_framework import serializers
from reviews.models import Review, Comment, Category, Genre, Titles

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ['id', 'author', 'score', 'text', 'pub_date']
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ['id', 'author', 'text', 'pub_date']
        model = Comment


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Genre


class TitlesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Titles
