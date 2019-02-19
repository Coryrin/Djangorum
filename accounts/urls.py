from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('<slug:username>/', views.user_profile, name='profile'),
    path('<slug:username>/create_mod', views.make_user_moderator, name="make_user_mod"),
]