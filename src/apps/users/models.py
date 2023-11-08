from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UsersModel(AbstractUser):
  username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
  email = models.EmailField(unique=True)
  name = models.CharField(max_length = 50)
  phone_number = PhoneNumberField(blank=True)
  
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name', 'username']


  def __str__(self):
      return "{}".format(self.email)