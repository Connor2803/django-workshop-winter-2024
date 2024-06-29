# post/views.py
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .utils import send_email


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["is_draft", "author"]
    search_fields = ["content", "author__username"]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:

            # Handle the case when the user is not authenticated
            # For example, you can raise an exception or set a default author
            # serializer.save(author=default_author)
            pass


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Get all comments for a specific post
        return Comment.objects.filter(post_id=self.kwargs["post_pk"])

    def perform_create(self, serializer):
        # Automatically set the author of a comment to the user making the request
        serializer.save(author=self.request.user)
        send_email("New Post Created", "A new post has been created on Snapstagram!", [
                   self.request.user.email])
