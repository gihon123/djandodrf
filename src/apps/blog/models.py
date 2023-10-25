from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
      return "{} - {}".format(self.title, self.author.name) 