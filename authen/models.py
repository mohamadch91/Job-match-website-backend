from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


class User(AbstractUser):
    username = models.CharField(null=True, unique=True, max_length=50, blank=True)
    phoneNumberRegex = RegexValidator(regex=r"^\+?98?\d{8,10}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=13, unique=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    birth = models.DateField(blank=True, null=True)
    gender = models.CharField(null=True, blank=True, max_length=1)
    registration_date = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    user_image = models.ImageField(null=True, blank=True, max_length=1024*1024*5)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return "{}".format(self.phone)
