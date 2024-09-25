from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post, User
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer,
    UserSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для управления объектами модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для управления объектами модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated,]

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для управления объектами модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated,]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для управления объектами модели User."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
