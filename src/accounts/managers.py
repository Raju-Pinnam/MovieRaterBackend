from django.contrib.auth.models import BaseUserManager
from django.utils.text import slugify

from ab_main.utils import get_rand_str


class UserManager(BaseUserManager):
    """User manager"""

    def create_user(self, username, email, password=None, **extra_fields):
        """Normal user's creating function"""
        if email is None:
            raise ValueError('email can\'t be None')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.slug = slugify(email) + get_rand_str(size=5)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staff_user(self, username, email, password, **extra_fields):
        """Staff user's creating function"""
        user = self.create_user(username=username, email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        """Super User creating function"""
        user = self.create_user(username=username, email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
