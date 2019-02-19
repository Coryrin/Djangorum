from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import ForumBoard, Post, PostComment
from .forms import PostForm, CommentForm
from accounts.models import UserProfile
from accounts.forms import UserProfileForm, UserCreateForm

# Check if the currently logged in user is either a moderator or a staff member
def staff_check(user):
    if user.userprofile.moderator or user.is_staff:
        return True

# Forum List
def list(request):

    list = ForumBoard.objects.all()

    user_signup_form = UserCreateForm
    user_profile_form = UserProfileForm

    context = {
        'list': list,
        'title': 'Djangorum',
        'user_signup_form': user_signup_form,
        'user_profile_form': user_profile_form
    }

    return render(request, 'boards/forum_list.html', context)

# thread lists within specified forum
def forum_detail(request, slug):
    detail = ForumBoard.objects.get(slug=slug)

    paginator = Paginator(detail.posts.all(), 10)

    page = request.GET.get('page')
    threads = paginator.get_page(page)

    context = {
        'detail': detail,
        'title': detail.title,
        'threads': threads
    }

    return render(request, 'boards/thread_list.html', context)

# thread detail view
def thread_detail(request, forum_slug, thread_slug):
    # Get the forum board the thread is located in
    forum = ForumBoard.objects.get(slug=forum_slug)
    # Get the thread where the thread_slug passed into the request is the same as the slug in the db
    thread = Post.objects.get(slug=thread_slug)

    thread.views += 1
    thread.save()

    user_prof = UserProfile.objects.get(user=thread.author)

    paginator = Paginator(thread.comments.all(), 10)

    page = request.GET.get('page')
    comments = paginator.get_page(page)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            # Set a comment variable to the form data, commit = false so that we can adjust data
            comment = comment_form.save(commit=False)
            # Set the "post" field on the model to the current thread the user is in
            # print(comment.body)
            comment.post = thread
            comment.author = request.user
            # Save the comment
            comment.save()
            return HttpResponseRedirect(reverse_lazy('boards:thread_detail', 
                                        kwargs={"forum_slug":forum.slug,
                                                'thread_slug': thread.slug}))

    else:
        comment_form = CommentForm

    context = {
        'forum': forum,
        'thread': thread,
        'title': thread.title,
        'comment_form': comment_form,
        'user_prof': user_prof,
        'comments': comments
    }

    return render(request, 'boards/thread_detail.html', context)

# Create a thread view
@login_required()
def create_thread(request, slug):
    
    current_forum = ForumBoard.objects.get(slug=slug)

    # Check if the request is a POST request
    if request.method == 'POST':
        
        # Get the form data that was posted
        form = PostForm(request.POST)

        # If the form is valid, save the data to the db and redirect to the newly created thread
        if form.is_valid():
            thread = form.save(commit=False)

            thread.forum = current_forum

            thread.author = request.user

            thread.save()

            return HttpResponseRedirect(reverse_lazy('boards:thread_detail',
                                        kwargs={"forum_slug": thread.forum.slug,
                                        "thread_slug": thread.slug}))
    else:

        form = PostForm

    context = {
        'form': form,
        'title': 'Create Thread'
    }

    return render(request, 'boards/create_thread.html', context)

# DELETE THREAD VIEW
@user_passes_test(staff_check)
def delete_thread(request, forum_slug, thread_slug):
    # Get the forum board the thread is located in
    forum = ForumBoard.objects.get(slug=forum_slug)
    # Get the thread where the thread_slug passed into the request is the same as the slug in the db
    thread = Post.objects.get(slug=thread_slug)

    thread.delete()

    return redirect('boards:list')

@user_passes_test(staff_check)
def delete_post(request, forum_slug, thread_slug, post_id):
    # Get the forum board the thread is located in
    forum = ForumBoard.objects.get(slug=forum_slug)
    # Get the thread where the thread_slug passed into the request is the same as the slug in the db
    thread = Post.objects.get(slug=thread_slug)

    post = PostComment.objects.get(id=post_id)

    post.delete()

    return HttpResponseRedirect(reverse_lazy('boards:thread_detail',
                                        kwargs={"forum_slug": thread.forum.slug,
                                        "thread_slug": thread.slug}))

