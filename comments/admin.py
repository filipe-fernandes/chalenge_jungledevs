"""
Comments admin
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
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at',)
    # inlines = [PostInline]
