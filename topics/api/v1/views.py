"""
API V1: Topics Views
"""
###
# Libraries
###
from rest_framework import viewsets,mixins, permissions
from . import serializers
from topics.models import Topic

###
# Filters
###


###
# Viewsets
###
class ListCreateTopicViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Topic.objects.all()
    def create(self,request):
        request.data['author']=request.user.id
        return super(ListCreateTopicViewSet,self).create(request)

class RetriveUpdateDeleteTopicViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.TopicSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Topic.objects.all()
    lookup_field = "url_name"
    
