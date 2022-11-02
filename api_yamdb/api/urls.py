from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework.authtoken import views
from .views import (CategoryViewSet, GenreViewSet, TitlesViewSet,
                    ReviewViewSet, CommentViewSet,
                    UserViewSet, get_jwt_token, register)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitlesViewSet, basename='titles')
router_v1.register('reviews', ReviewViewSet, basename='reviews')
router_v1.register('comments', CommentViewSet, basename='comments')
router_v1.register(r'users', UserViewSet)

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
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]



