from django.shortcuts import render
from .models import blog_post

# Create your views here.
def blogpage(request):
    all_posts = blog_post.objects.all()
    return render(request, 'blog/blog.html', {'all_posts':all_posts})