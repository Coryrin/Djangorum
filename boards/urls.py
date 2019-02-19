from django.urls import path, re_path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.list, name='list'),
    path('<slug:slug>/', views.forum_detail, name='forum_detail'),
    path('<slug:forum_slug>/<slug:thread_slug>', views.thread_detail, name='thread_detail'),
    path('<slug:slug>/create_thread/', views.create_thread, name='create_thread'),
    path('<slug:forum_slug>/<slug:thread_slug>/delete', views.delete_thread, name="delete_thread"),
    path('<slug:forum_slug>/<slug:thread_slug>/<int:post_id>/delete', views.delete_post, name="delete_post")
]