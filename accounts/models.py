from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    sign_up_date = models.DateField(auto_now_add=True)

    moderator = models.BooleanField(default=False, blank=True)

    profile_pic = models.ImageField(blank=True, upload_to='profile_pics')

    def __str__(self):
        return "{}'s Profile".format(self.user.username)

    class Meta:
        verbose_name_plural = 'User Profiles'
