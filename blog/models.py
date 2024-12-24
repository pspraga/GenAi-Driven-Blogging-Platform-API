# blog/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
#from django.contrib.auth.models import User


class BlogPost(models.Model):
    # Fields as before...

    class Meta:
        permissions = [
            ('can_create_blog', 'Can create blog posts'),
            ('can_edit_blog', 'Can edit blog posts'),
            ('can_delete_blog', 'Can delete blog posts'),
        ]

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    roles = models.ManyToManyField(Role)

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, related_name="articles", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        permissions = [
            ('can_view_article', 'Can view articles'),
            ('can_edit_article', 'Can edit articles'),
            ('can_delete_article', 'Can delete articles'),
        ]
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.article.title}"
    

