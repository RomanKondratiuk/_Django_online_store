from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(verbose_name='avatar', **NULLABLE)
    phone_number = models.CharField(max_length=35, verbose_name='phone_number', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='country', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
