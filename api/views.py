from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from boards.models import ForumBoard
from .serializers import ForumBoardSerializer

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