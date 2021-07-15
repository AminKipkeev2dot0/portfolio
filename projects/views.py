from django.shortcuts import render
from .models import project

# Create your views here.
def home(request):
    all_projects = project.objects.all()
    return render(request, 'projects/home.html', {'all_projects': all_projects})