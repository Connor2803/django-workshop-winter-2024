from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostCommentViewSet


router = DefaultRouter()
router.register(r"", PostViewSet, basename="posts")
router.register(
    r"(?P<post_pk>[^/.]+)/comments", PostCommentViewSet, basename="comments"
)

urlpatterns = [
    path("", include(router.urls)),
]
