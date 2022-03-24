from django.urls import path, include
from .views import (
    ForumBoardViewSet,
    ForumBoardDetailView,
    ThreadDetailView
)

app_name = 'api'

urlpatterns = [
    path('', ForumBoardViewSet.as_view()),
    path('<slug:slug>', ForumBoardDetailView.as_view()),
    path('<slug:slug>/<int:id>', ThreadDetailView.as_view()),
]