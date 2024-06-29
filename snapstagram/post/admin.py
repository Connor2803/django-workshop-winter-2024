from django.contrib import admin
from .models import Post, Comment, Image


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "is_draft", "created_at", "updated_at", "author")
    list_filter = ("is_draft", "created_at", "updated_at", "author")
    search_fields = ("content", "author__username")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "post",
        "parent_comment",
        "created_at",
        "updated_at",
        "author",
    )
    list_filter = ("post", "parent_comment", "created_at", "updated_at", "author")
    search_fields = ("content", "author__username")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "post")
    list_filter = ("post",)
    search_fields = ("url",)
    ordering = ("id",)
