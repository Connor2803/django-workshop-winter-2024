
# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Post
from django.urls import reverse


# Test all HTTP methods for `PostViewSet`
class PostTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        data = {"content": "Hello, World!"}
        url = reverse("posts-list")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().content, "Hello, World!")

    def test_list_posts(self):
        Post.objects.create(content="Hello, World!")
        Post.objects.create(content="Hello, Django!")
        url = reverse("posts-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_post(self):
        post = Post.objects.create(content="Hello, World!")
        url = reverse("posts-detail", args=[post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], "Hello, World!")

    def test_delete_post(self):
        post = Post.objects.create(content="Hello, World!")
        url = reverse("posts-detail", args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Post.objects.count(), 0)
