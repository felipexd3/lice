"""
modelo custom user
"""
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserManager(BaseUserManager):
    """
    manipulação da  classe usuario
    """

    def create_user(self, first_name, last_name, email, password=None):
        """
        criação usuario padrão
        """
        if not email:
            raise ValueError('Campo Obrigatório')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, first_name, last_name, email, password):
        """
        criação staff user
        """
        user = self.create_user(first_name, last_name, email, password=password,)
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        """
        criação admin user
        """
        user = self.create_user(first_name, last_name, email, password=password,)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    custom user, usando email como login e nao utilizando username
    """

    username_validator = UnicodeUsernameValidator()

    #username como true, pq se não utilizar, dá erro
    username = models.CharField(verbose_name='Usuário', max_length=15, unique=True, null=True, validators=[username_validator])
    first_name = models.CharField(verbose_name='Nome', max_length=20)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=20)
    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True)
    active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

def get_full_name(self):
    """
    retorna nome completo usuario
    """
    full_name = '%s %s' %(self.first_name, self.last_name)
    return full_name.strip()

def get_short_name(self):
    """
    sobrescrição me short_name do user padrão
    """
    return self.first_name

def __str__(self):
    return self.email

def has_perm(self, perm, obj=None):
    """
    next
    """
    return True

def has_module_perms(self, app_label):
    """
    next
    """
    return True

@property
def is_staff(self):
    """
    next
    """
    return self.is_staff

@property
def is_admin(self):
    """
    next
    """
    return self.is_admin

@property
def is_active(self):
    """
    next
    """
    return self.active
