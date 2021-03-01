"""
API V1: Comments Serializers
"""
###
# Libraries
###
from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=["title","post","content"]#,"url_name"
        

