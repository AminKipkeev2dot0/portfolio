from django.db import models

# Create your models here.
class blog_post(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=10000)
    dateofpost = models.DateField(auto_now=False, auto_now_add=False)
    ordering = ['-id']

    def __str__ (self):
        return self.title