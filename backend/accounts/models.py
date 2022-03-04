from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
   """
      here we specifying the methods of creating users and superusers
   """
   def create_user(self, email, name, password=None):
      """
         password=None => to prevent creating a user without password
      """
      if not email:
         raise ValueError('Users must have an email address')
      email = self.normalize_email(email)
      user = self.model(email=email, name=name)
      user.set_password(password)
      user.save()
      return user

   

class UserAccount(AbstractBaseUser, PermissionsMixin):
   # we will use this email field as a login field instead of the default
   # username field provided by django, and we will use this field also 
   # in USERNAME_FIELD and all fields of this field must be marked as unique
   email = models.EmailField(max_length=255, unique=True)
   
   name = models.CharField(max_length=255)

   is_active = models.BooleanField(default=True)

   is_staff = models.BooleanField(default=False)

   USERNAME_FIELD = 'email'

   # all fields you need to be required when you use 
   # >> python manage.py createsuperuser
   REQUIRED_FIELDS= ['name']

   def get_full_name(self):
      return self.name

   def get_short_name(self):
      return self.name
   
   def __str__(self):
      return self.email

   objects= UserAccountManager()
