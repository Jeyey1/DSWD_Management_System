from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_buyer = models.BooleanField(default=False, verbose_name ="....")
    is_supplier = models.BooleanField(default=False, verbose_name ="is staff")
    is_admin = models.BooleanField(default=False)