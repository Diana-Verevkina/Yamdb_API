from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, mixins
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CategorySerializer, GenreSerializer, TitlesSerializer
from reviews.models import Category, Genre, Titles, Review, Comment

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category__slug', 'genre__slug', 'name', 'year')


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
