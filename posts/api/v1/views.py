"""
API V1: Posts Views
"""
###
# Libraries
###
from rest_framework import viewsets,mixins, permissions
from . import serializers
from posts.models import Post

###
# Filters
###


###
# Viewsets
###
class ListCreatePostViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    def create(self,request):
        request.data['author']=request.user.id
        return super(ListCreatePostViewSet,self).create(request)

class RetriveUpdateDeletePostViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    # lookup_field = "url_name"
    
