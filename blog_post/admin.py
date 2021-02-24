from django.contrib import admin
from blog_post.models import Category, Tag, BlogPost, BlogComment
# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(BlogPost)
admin.site.register(BlogComment)