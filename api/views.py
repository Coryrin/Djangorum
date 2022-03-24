from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from boards.models import ForumBoard, Post
from .serializers import ForumBoardSerializer, ThreadSerializer

class ForumBoardViewSet(APIView):
    def get(self, request, *args, **kwargs):
        forums = ForumBoard.objects.all()
        serializer = ForumBoardSerializer(forums, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ForumBoardDetailView(APIView):
    def get(self, request, slug, *args, **kwargs):
        forum = ForumBoard.objects.get(slug=slug)

        if not forum:
            return Response(
                {
                    "result": f"Object with slug {slug} does not exist."
                }
            )

        serializer = ForumBoardSerializer(forum)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ThreadDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        thread = Post.objects.get(id=id)

        if not thread:
            return Response(
                {
                    "result": f"Object with id {id} does not exist."
                }
            )
        
        serializer = ThreadSerializer(thread)

        return Response(serializer.data, status=status.HTTP_200_OK)
