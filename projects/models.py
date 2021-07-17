from django.db import models

# Create your models here.
class project (models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to="images")
    url = models.URLField(blank=True)

    def __str__ (self):
        return self.title