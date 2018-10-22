from django.contrib.auth.models import User as Auth_User
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
class User(Auth_User, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)