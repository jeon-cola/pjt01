from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # 게시글 관련 URL
    path('articles/', views.article_list, name='article_list'),  # 게시글 목록 조회 및 생성
    path('articles/<int:article_pk>/', views.article_detail, name='article_detail'),  # 특정 게시글 조회, 수정, 삭제
    
    # 댓글 관련 URL
    path('comments/', views.comment_list, name='comment_list'),  # 모든 댓글 조회
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),  # 특정 댓글 조회, 수정, 삭제
    path('articles/<int:article_pk>/comments/', views.comment_create, name='comment_create'),  # 특정 게시글에 댓글 생성
]