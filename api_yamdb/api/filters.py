from django_filters import rest_framework as filters
from reviews.models import Titles


class TitlesFilter(filters.FilterSet):
    genre = filters.CharFilter(lookup_expr='slug')
    category = filters.CharFilter(lookup_expr='slug')
    name = filters.CharFilter(lookup_expr='icontains')
    # year = filters.CharFilter(lookup_expr='year')

    class Meta:
        model = Titles
        fields = ['genre', 'category', 'name', 'year']