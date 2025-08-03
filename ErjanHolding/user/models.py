from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from product.constants import NULLABLE
from user.choices import MyUserRoleEnum


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):

        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)

        return user



class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=222,verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name = 'Адрес электронной почты')
    avatar = models.ImageField(upload_to='media/user_avatar', **NULLABLE, verbose_name='Аватар')
    role = models.CharField(
        max_length=20,
        choices=MyUserRoleEnum.choices,
        default=MyUserRoleEnum.STANDARD_USER,
        verbose_name='Роль'
    )
    balance = models.DecimalField(default=0, decimal_places=2,max_digits=12,verbose_name='Баланс')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return {self.email}

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_stuff(self):
        return self.is_admin
