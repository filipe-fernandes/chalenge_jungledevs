"""
Comments Models
"""

from django.db import models
from helpers.models import TimestampModel
from posts.models import Post


class Comment(TimestampModel):
    title = models.CharField(max_length=64,null=False,blank=False,unique=True)
    post = models.ForeignKey(Post,null=False,on_delete=models.CASCADE)
    content = models.TextField(max_length=500,null=False,blank=False)
    # url_name = models.SlugField(max_length=30,null=False,blank=False,unique=True)