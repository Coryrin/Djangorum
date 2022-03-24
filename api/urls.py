from django.urls import path, include
from .views import (
    ForumBoardViewSet,
    ForumBoardDetailView
)

app_name = 'api'

urlpatterns = [
    path('', ForumBoardViewSet.as_view()),
    path('<slug:slug>', ForumBoardDetailView.as_view()),
]