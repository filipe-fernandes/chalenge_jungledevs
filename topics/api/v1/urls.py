"""
API V1: Accounts Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers

from .views import ListCreateTopicViewSet,RetriveUpdateDeleteTopicViewSet
###
# Routers
###
""" Main router """
router = routers.SimpleRouter()
router.register(prefix="topics",viewset=ListCreateTopicViewSet, basename='topics')
router.register(prefix="topics",viewset=RetriveUpdateDeleteTopicViewSet, basename='topics')
###
# URLs
###
urlpatterns = [
    url(r'^', include(router.urls)),
]
