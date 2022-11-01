from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from reviews.models import Category, Genre, Titles, Review, Comment


class CategoryViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class TitlesViewSet(viewsets.ModelViewSet):
    pass


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
