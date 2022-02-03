from django.db import models
from django.contrib import auth
from django.urls import reverse
# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):
    

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "contact:displaycontacts",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )
    


    