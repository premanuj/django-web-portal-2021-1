from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class BlogPost(models.Model):
    tilte = models.CharField(max_length=255)
    slug = models.SlugField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(Category, related_name='blog_categories')
    tags = models.ManyToManyField(Tag, related_name="blog_tags")
    content = models.TextField()
    viewer = models.IntegerField(default=0)
    cover_image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class BlogComment(models.Model):
    blog_post = models.ForeignKey(BlogComment)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)