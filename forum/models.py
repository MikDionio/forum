import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_title=models.CharField(max_length=50)
    post_text=models.CharField(max_length=1000)
    post_author=models.CharField(max_length=30)
    post_pubdate=models.DateTimeField('date posted')
    def __str__(self):
        return self.post_text

class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text=models.CharField(max_length=50)
    comment_pubdate=models.DateTimeField('date commented')
    comment_author = models.CharField(max_length = 30)
    def __str__(self):
        return self.comment_text
