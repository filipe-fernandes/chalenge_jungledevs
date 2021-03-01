"""
API V1: Posts Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=["title","topic","content"]#,"url_name"
        

