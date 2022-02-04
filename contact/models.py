
from django.conf import settings
from django.forms import CharField
from django.urls import reverse
from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth import get_user_model
User = get_user_model()


class UserContactModel(models.Model):

    avail_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{2,15}$', message="Phone number must contain only numbers. Up to 15 digits allowed.")

    user = models.ForeignKey(
        User, related_name="foruser", on_delete=models.CASCADE)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    nickname = models.CharField(max_length=25, blank=True)
    gender = models.CharField(max_length=7, choices=avail_gender, blank=True)
    address = models.CharField(max_length=125, blank=True)
    phone_number = models.CharField(max_length=15, validators=[
                                    phone_regex], blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["firstname"]
