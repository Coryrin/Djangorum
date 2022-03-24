from django.contrib.auth.models import User
from rest_framework import serializers
from boards import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ThreadSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = models.Post
        fields = ['title', 'body', 'author']

class ForumBoardSerializer(serializers.ModelSerializer):
    posts = ThreadSerializer(many=True, read_only=True)

    class Meta:
        model = models.ForumBoard
        fields = ['title', 'description', 'slug', 'posts']
