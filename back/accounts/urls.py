from django.urls import path
from .views import SignUpView, ProfileView, LoginView, LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),  # 로그인 경로 추가
    path('logout/', LogoutView.as_view(), name='logout'),
]
