"""
API V1: Comments Views
"""
###
# Libraries
###
from rest_framework import viewsets,mixins, permissions
from . import serializers
from comments.models import Comment

###
# Filters
###


###
# Viewsets
###
class ListCreateCommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    def create(self,request):
        request.data['author']=request.user.id
        return super(ListCreateCommentViewSet,self).create(request)

class RetriveUpdateDeleteCommentViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Comment.objects.all()
    # lookup_field = "url_name"
    
