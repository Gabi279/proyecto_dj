from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    SUPERUSUARIO = '0'
    ADMIN = '1'
  
    ROL_CHOICES = [
        (SUPERUSUARIO, 'Superusuario'),
        (ADMIN, 'Administrador'),
    ]
    auto_increment_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField()
    rol = models.CharField(
        max_length=1, 
        choices=ROL_CHOICES, 
        blank=True
    )
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    def __str__(self):
        return self.username