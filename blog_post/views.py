from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from blog_post.models import Category, Tag, BlogPost
from django.http import JsonResponse
from django.utils.decorators import method_decorator
# Create your views here.

class BlogPostView(TemplateView):
    template_name = "blog_post/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["tags"] = Tag.objects.all()
        posts = BlogPost.objects.all().order_by('-created_at')
        context["latest_posts"] = posts if len(posts) < 3 else posts[:3]
        context["popular_posts"] = BlogPost.objects.all().order_by('-viewer')
        return context

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blog_post/post.html"
    fields = ('title', 'content', 'tags', 'categories', 'cover_image')


# class CategoryRelatedPostList(ListView):
#     model = Category
#     context_object_name = 'categories'
#     template_name='blog_post/category_posts.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[""] = 
    #     return context

class CategoryRelatedPostDetail(DetailView):
    model = Category
    context_object_name = 'category' # default object
    template_name='blog_post/category_posts.html'


# @method_decorator(methods = ["GET"])
def get_tags(request):
    tags = Tag.objects.all()

        

    