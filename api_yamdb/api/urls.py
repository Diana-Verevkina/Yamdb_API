from django.urls import include, path
from rest_framework import routers

from .views import CategoryViewSet, GenreViewSet, TitlesViewSet, ReviewViewSet, CommentViewSet
from rest_framework.authtoken import views

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitlesViewSet, basename='titles')
router_v1.register('reviews', ReviewViewSet, basename='reviews')
router_v1.register('comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(
        'v1/titles/<int:title_id>/',
        include(router_v1.urls),
        name='reviews'
    ),
    path(
        'v1/titles/<int:title_id>/reviews/<int:review_id>/',
        include(router_v1.urls),
        name='comments'
    ),
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
