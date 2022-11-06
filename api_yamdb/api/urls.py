from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import (CategoryViewSet, GenreViewSet, get_jwt_token,
                    TitlesViewSet, register, ReviewViewSet, CommentViewSet,
                    UserViewSet)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitlesViewSet, basename='titles')
router_v1.register(r'users', UserViewSet)


review_router = routers.NestedSimpleRouter(router_v1, r'titles',
                                           lookup='title')
review_router.register(r'reviews', ReviewViewSet, basename='review')

comment_router = routers.NestedSimpleRouter(review_router, r'reviews',
                                            lookup='review')
comment_router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include(review_router.urls)),
    path('v1/', include(comment_router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
