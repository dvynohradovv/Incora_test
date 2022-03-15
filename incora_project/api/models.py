import phonenumbers
from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import ValidationError
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name"]

    @staticmethod
    def validate_first_name(data):
        for char in data:
            if not char.isalpha():
                raise ValidationError("Only letters!")
        return data

    @staticmethod
    def validate_last_name(data):
        for char in data:
            if not char.isalpha():
                raise ValidationError("Only letters!")
        return data

    @staticmethod
    def validate_phonenumber(data):
        if data == "":
            return data
        try:
            pn = phonenumbers.parse(data)
        except Exception as exc:
            raise ValidationError(exc)
        if not phonenumbers.is_valid_number(pn):
            raise ValidationError("Invalid phone number")
        return data
