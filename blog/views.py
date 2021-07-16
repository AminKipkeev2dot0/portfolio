from django.shortcuts import render, get_object_or_404
from .models import blog_post

# Create your views here.
all_posts = blog_post.objects.all()
def blogpage(request):
    #all_posts = blog_post.objects.all()
    return render(request, 'blog/blog.html', {'all_posts':all_posts})

def detail(request, blog_id):
    blog = get_object_or_404(blog_post, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})