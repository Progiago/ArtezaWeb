from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class Usuario(AbstractBaseUser):
    username = models.CharField
    email = models.EmailField(verbose_name="email", unique=True)
    USERNAME_FIELD = "email"
    