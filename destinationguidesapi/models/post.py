from django.db import models
from .user import User
from .category import Category
from .country import Country
from .region import Region
from .tag import Tag

class Post(models.Model):
  
  title = models.CharField(max_length=50)
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  body = models.CharField(max_length=280)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  region = models.ForeignKey(Region, on_delete=models.CASCADE)
  image = models.URLField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ("-created_at", "region", "country")
