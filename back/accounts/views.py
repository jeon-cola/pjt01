# accounts/views.py
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework.exceptions import ValidationError

User = get_user_model()

# 회원가입 뷰
class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 프로필 뷰
class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

#로그인 뷰
class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'error': 'Invalid credentials', 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # 예기치 않은 오류가 발생할 경우 서버 로그에 출력하여 디버깅에 도움을 줍니다.
            print(f"Unexpected error: {str(e)}")
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 로그아웃
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # 현재 사용자의 토큰을 가져와 삭제합니다.
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token or already logged out.'}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # 현재 요청한 사용자 객체를 반환
        return self.request.user