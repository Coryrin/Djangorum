from django.contrib import admin
from .models import ForumBoard, Post, PostComment

class ForumBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'body', 'views', 'author', 'created_at')

    list_filter = ['forum']

class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'body', 'author')

admin.site.register(ForumBoard, ForumBoardAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)

admin.site.site_header = "Djangorum"

admin.site.index_title = "Djangorum Administration"