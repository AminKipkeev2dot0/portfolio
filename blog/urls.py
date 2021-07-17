from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'blog'
urlpatterns =[
    path('', views.blogpage, name = 'blogpage'),
    path('<int:blog_id>', views.detail, name= 'detail')
]