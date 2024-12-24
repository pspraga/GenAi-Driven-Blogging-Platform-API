# blog/views.py
from rest_framework.permissions import BasePermission
# blog/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost, Comment, CustomUser
from .serializers import BlogPostSerializer, CommentSerializer, UserSerializer
from .permissions import IsAdminOrEditor
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.decorators import action
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseForbidden
from .models import Article
from django.contrib.auth.decorators import permission_required
@permission_required('blog.can_view_article', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

@permission_required('blog.can_edit_article', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Logic for editing the article
    return render(request, 'articles/edit.html', {'article': article})

def delete_article(request, pk):
    # Check if the user has the 'can_delete_article' permission
    if not request.user.has_perm('blog.can_delete_article'):
        return HttpResponseForbidden("You do not have permission to delete this article.")
    
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can post articles

    def perform_create(self, serializer):
        # Automatically set the author to the current logged-in user
        serializer.save(author=self.request.user)
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminOrEditor]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    # Custom action to get comments for a specific article
    @action(detail=True, methods=['get'], url_path='comments')
    def get_comments(self, request, pk=None):
        article = self.get_object()
        comments = article.comments.all()  # Get all comments for the article
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class IsAdminOrEditor(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.has_perm('blog.can_create_blog') or user.has_perm('blog.can_edit_blog') or user.has_perm('blog.can_view_article')
