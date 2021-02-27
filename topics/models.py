"""
Topics Models
"""

from django.db import models
from helpers.models import TimestampModel
from accounts.models import User

class Topic(TimestampModel):
    name = models.CharField(max_length=64,null=False,blank=False,unique=True)
    title = models.CharField(max_length=64,null=False,blank=False,unique=True)
    author = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    description = models.TextField(max_length=300,null=False,blank=False)
    url_name = models.SlugField(max_length=30,null=False,blank=False,unique=True)
