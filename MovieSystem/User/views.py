from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

@api_view(['POST'])
@permission_classes([AllowAny])
def user_registration(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=400)

    user, created = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.save()

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return Response({'access_token': access_token})
