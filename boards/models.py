from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class ForumBoard(models.Model):
    
    # Board fields
    title = models.CharField(max_length=255)
    description = models.TextField()

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Slugify the title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Forums'


# POST WITHIN EACH BOARD
class Post(models.Model):
    forum = models.ForeignKey(ForumBoard, on_delete=models.CASCADE, related_name='posts')

    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    title = models.CharField(max_length=255)

    body = models.TextField()

    views = models.IntegerField(default=0)

    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        # Order threads by amount of views they have
        ordering = ['-views']
        verbose_name_plural = 'Posts'


# REPLIES TO EACH POST
class PostComment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50] + '...'

    class Meta:
        verbose_name_plural = 'Thread Replies'