from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from .models import UserProfile
from boards.models import Post
from boards.views import staff_check
from . import forms

# sign up view
def signup_view(request):
    
    # If the request method is post, that means a user submitted the sign up form
    if request.method == 'POST':

        # Get the data from the input form
        user_form = forms.UserCreateForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST, request.FILES)

        # Check that all the data is valid
        if user_form.is_valid() and profile_form.is_valid():
            # Set the user, hash the password
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Once the user has been saved, log them in and redirect back to the home page
            user = authenticate(request, username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])

            login(request, user)

            messages.success(request, "Successfully signed up.")

            return redirect('boards:list')

    else:

        user_form = forms.UserCreateForm
        profile_form = forms.UserProfileForm

    context = {
        'title': 'Sign Up',
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'accounts/signup.html', context)

def login_view(request):
    
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user with the passed in credentials
        user = authenticate(request, username=username, password=password)

        # Check the user actually exists
        if user is not None:
            login(request, user)

            messages.success(request, "Successfully logged in!")
            return redirect('boards:list')
            
        # If there was an error loggin in - e.g., wrong username/password 
        else:
            messages.warning(request, "There was an error logging you in. Please check your email and password and try again.")

    context = {
        'title': 'Log In'
    }

    return render(request, 'accounts/login.html', context)

# logout
def logout_view(request):
    # Log the user out and redirect them to the forum list page
    logout(request)
    messages.success(request, "You have been logged out. Thanks for visiting!")
    return redirect('boards:list')

# Individual user profiles. Displaying threads they've created
def user_profile(request, username):
    
    user_prof = User.objects.get(username=username)
    user_threads = Post.objects.filter(author=user_prof)


    context = {
        'title': user_prof.username,
        'user_prof': user_prof,
        'user_threads': user_threads
    }

    return render(request, 'accounts/user_profile.html', context)

# view to change a given user to a moderator
@user_passes_test(staff_check)
def make_user_moderator(request, username):
    user = User.objects.get(username=username)
    # set the "moderator" field on the UserProfile model to true
    user.userprofile.moderator = True
    # save the new updated info
    user.userprofile.save()

    messages.success(request, 'Successfully made {} a moderator.'.format(username))

    return redirect("boards:list")