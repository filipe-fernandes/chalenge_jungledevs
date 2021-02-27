"""
Accounts admin
"""
###
# Libraries
###
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models


###
# Inline Admin Models
###

# class PostInline(admin.StackedInline):
#     model = Post
#     extra = 1
###
# Main Admin Models
###
@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'author', 'description', 'url_name', 'created_at', 'updated_at',)
    # inlines = [PostInline]
