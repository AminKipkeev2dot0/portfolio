from django.shortcuts import render
from .models import project
from blog.models import blog_post

# Create your views here.
def home(request):
    all_posts = blog_post.objects.all()[-1:-3]
    all_projects = project.objects.all()
    return render(request, 'projects/home.html', {'all_projects': all_projects, 'all_posts':all_posts})