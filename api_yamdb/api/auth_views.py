from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.db.utils import IntegrityError
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from reviews.models import User
from .serializers import RegisterDataSerializer, TokenSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user, _ = User.objects.get_or_create(**serializer.data)
    except IntegrityError as err:
        raise ValidationError(str(err))

    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject='YaMDb регистрация',
        message=f'Ваш код подтверждения: {confirmation_code}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )

    if default_token_generator.check_token(
        user, serializer.validated_data['confirmation_code']
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)}, status=HTTP_200_OK)

    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)