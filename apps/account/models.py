from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    class Role(models.TextChoices):
        MAINTAINER = 'maintainer', 'Maintainer'
        DEVELOPER = 'developer', 'Developer'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.DEVELOPER)


class AccountLogin(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, verbose_name="Session Key")



