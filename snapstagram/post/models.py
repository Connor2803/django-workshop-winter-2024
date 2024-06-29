from django.db import models
import uuid
from django.contrib.auth.models import User
from django.forms import ValidationError


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    is_draft = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )

    def __str__(self):
        # Format when printed: Post ID (Author): Content
        return f"Post {self.id} ({self.author}): {self.content[:30]}"


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    # When a comment is a reply to another comment, this field will be set
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        # Format when printed: Comment ID (Author): Content
        return f"Comment {self.id} ({self.author}): {self.content[:30]}"

    def clean(self):
        if self.parent_comment == self:
            raise ValidationError("A comment cannot be a reply to itself")
        if self.parent_comment and self.parent_comment.post != self.post:
            raise ValidationError(
                "Parent comment must belong to the same post")


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"Image {self.id} for Post {self.post.id}"

    def clean(self):
        accepted_extensions = [".png", ".jpg", ".jpeg", ".gif"]
        if not self.url.endswith(tuple(accepted_extensions)):
            raise ValidationError(
                f"Invalid image URL. Must end with any of {
                    accepted_extensions}"
            )
