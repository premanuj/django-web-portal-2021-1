
from django.urls import path
from blog_post.views import BlogPostView, BlogPostCreateView, get_tags

urlpatterns = [
    path('', BlogPostView.as_view(), name='blog'),
    path('create/', BlogPostCreateView.as_view(), name='create_post'),
    # path('get_tags/', get_tags, name='get_tags'),
]
