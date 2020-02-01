from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.text import slugify

from .managers import UserManager
from ab_main.utils import get_file_ext, get_rand_str


def profile_pic_upload_path(instance, file):
    """Passing path of user profile pic"""
    email = slugify(instance.email)[:3]
    filename, ext = get_file_ext(file)
    new_filename = f'{email}-{get_rand_str(size=3).lower()}{ext}'
    final_path = f'users/profiles/{email}/{new_filename}'
    return final_path


class User(AbstractUser, PermissionsMixin):
    """Main custom user details"""
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=255, unique=True)
    slug = models.SlugField(max_length=120, null=True, blank=True)
    profile_pic = models.ImageField(upload_to=profile_pic_upload_path, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    user_updated = models.DateTimeField(auto_now=True)
    user_created = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['username', ]
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
