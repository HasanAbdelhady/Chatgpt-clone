from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=False)
    profile_image = models.ImageField(
        upload_to='profile_images/', blank=True, null=True
    )

    def __str__(self):
        return self.email
