"""
API V1: Posts Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from topics.api.v1.urls import router

from .views import ListCreatePostViewSet,RetriveUpdateDeletePostViewSet
###
# Routers
###
""" Main router """

posts_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
# router = routers.SimpleRouter()
posts_router.register(prefix="posts",viewset=ListCreatePostViewSet, basename='posts')
posts_router.register(prefix="posts",viewset=RetriveUpdateDeletePostViewSet, basename='posts')
###
# URLs
###
urlpatterns = [
    url(r'^', include(posts_router.urls)),
]
