from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from apps.mycountry.models import *


class Token(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    key = models.CharField(max_length=255, unique=True)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError("Le nom d'utilisateur est requis.")
        if not email:
            raise ValueError("L'adresse e-mail est requise.")

        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user




class User(AbstractUser):
    tel = PhoneNumberField(
        null = True, 
        blank=True, 
        verbose_name = 'Tel', 
        help_text = 'Internatinal format: +229XXXXXXXX')
    
    
class Token(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    key = models.CharField(max_length=255, unique=True)

class MyAddress(models.Model):
    
    user = models.ForeignKey(User, verbose_name="Propriétaire", on_delete=models.CASCADE)
    adresse = models.ForeignKey(Adresse, verbose_name="Adresse", on_delete=models.CASCADE)
    precision = models.TextField(verbose_name="Precision", null = True, blank = True)
    
    class Meta:
        verbose_name ="Address"
        verbose_name_plural = "Address"

    def __str__(self):
        return str(self.user)
