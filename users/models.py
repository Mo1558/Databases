from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self,mobile, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(mobile, password, **other_fields)


    def create_user(self,mobile,  password, **other_fields):
        if not mobile:
            raise ValueError('You must provide an mobile number')

        
        user = self.model(mobile=mobile, **other_fields)
        user.set_password(password)
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length = 100)
    mobile = models.CharField(max_length=20, unique = True)
    email = models.EmailField(max_length = 80,blank=True,null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'mobile'
