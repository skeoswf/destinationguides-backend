from django.db import models
from .post import Post
from .user import User

class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
