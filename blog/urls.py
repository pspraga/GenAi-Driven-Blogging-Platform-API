# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny  # Allows any user to access the documentation
from blog.views import BlogPostViewSet, CommentViewSet, UserViewSet
from .views import ArticleViewSet
# Create the schema view with public access
schema_view = get_schema_view(
    openapi.Info(
        title="GenAI Blogging API",
        default_version='v1',
        description="API documentation for the GenAI blogging platform",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@genai.com"),
    ),
    public=True,
    permission_classes=[AllowAny],  # Allow any user to access the documentation
)

# Create the router and register viewsets
router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'users', UserViewSet)
router.register(r'articles', ArticleViewSet)

# Define the URL patterns
urlpatterns = [
    path('swagger/', schema_view.as_view(), name='swagger'),  # Swagger endpoint
    path('api/', include(router.urls)),
]
