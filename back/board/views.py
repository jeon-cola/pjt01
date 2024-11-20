from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

    def check_object_permissions(self, request, obj):
        if self.action in ['update', 'partial_update', 'destroy']:
            if obj.author != request.user:
                self.permission_denied(request, "본인의 게시물만 수정 또는 삭제할 수 있습니다.")
        super().check_object_permissions(request, obj)
