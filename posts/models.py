"""
Topics Models
"""

from django.db import models
from helpers.models import TimestampModel
from topics.models import Topic
from accounts.models import User

class Post(TimestampModel):
    title = models.CharField(max_length=64,null=False,blank=False,unique=True)
    topic = models.ForeignKey(Topic,null=False,on_delete=models.CASCADE)
    content = models.TextField(max_length=500,null=False,blank=False)
    author =  models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    # url_name = models.SlugField(max_length=30,null=False,blank=False,unique=True)