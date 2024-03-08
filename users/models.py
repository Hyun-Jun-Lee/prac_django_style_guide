import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from core.models import BaseModel
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email: str, is_active: bool = True, is_admin: bool = False, password=None
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email.lower()),
            is_active=is_active,
            is_admin=is_admin,
        )

        if not password:
            raise ValueError("Users must have a password")
        user.set_password(password)

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_super_user(self, email: str, password=None):
        user = self.create_user(
            email=email, is_active=True, is_admin=True, password=password
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    jwt_key = models.UUIDField(default=uuid.uuid4)

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin
