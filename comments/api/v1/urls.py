"""
API V1: Comments Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from posts.api.v1.urls import posts_router

from .views import ListCreatePostViewSet,RetriveUpdateDeletePostViewSet
###
# Routers
###
""" Main router """

comments_router = routers.NestedSimpleRouter(posts_router, r'posts', lookup='post')
# router = routers.SimpleRouter()
comments_router.register(prefix="comments",viewset=ListCreateCommentViewSet, basename='comments')
comments_router.register(prefix="comments",viewset=RetriveUpdateDeleteCommentViewSet, basename='comments')
###
# URLs
###
urlpatterns = [
    url(r'^', include(comments_router.urls)),
]
