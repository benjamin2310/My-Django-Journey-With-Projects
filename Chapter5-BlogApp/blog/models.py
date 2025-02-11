from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description = models.TextField()
    date_of_post = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={"pk": self.pk})  