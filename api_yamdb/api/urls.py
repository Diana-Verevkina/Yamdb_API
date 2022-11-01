from django.urls import include, path
from rest_framework import routers
from .views import (CategoryViewSet, GenreViewSet, TitlesViewSet,
                    UserViewSet, get_jwt_token, register)

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('titles', TitlesViewSet, basename='titles')
router_v1.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
