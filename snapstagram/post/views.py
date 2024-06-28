from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsAuthorOrReadOnly
from .utils import send_email


class PostCommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Get all comments for a specific post
        return Comment.objects.filter(post_id=self.kwargs["post_pk"])

    def perform_create(self, serializer):
        # Automatically set the author of a comment to the user making the request
        serializer.save(author=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["is_draft", "author"]
    search_fields = ["content", "author__username"]
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        # Automatically set the author of a post to the user making the request
        serializer.save(author=self.request.user)
        send_email("New Post Created", "A new post has been created on Snapstagram!", [self.request.user.email])
