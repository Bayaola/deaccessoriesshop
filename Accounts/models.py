from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
import time
from .utils import MEMBERSHIP_CHOICES
# Create your models here.

from pyuploadcare.dj.models import ImageField


class AccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, phone, password, **extra_fields):
        values = [email, name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, name, phone, password=None, **extra_fields):
        # extra_fields.setdefault('is_premium', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, name, phone, password, **extra_fields)


    def create_superuser(self, email, name, phone, password=None, **extra_fields):
        # extra_fields.setdefault('is_premium', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # if extra_fields.get('is_premium') is not True:
        #     raise ValueError('Superuser must have is_premium=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, phone, password, **extra_fields)


class Membership(models.Model):
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES, default='Free', max_length=30
    )
    slug = models.SlugField(null=True, blank=True)
    # slug = models.SlugField(max_length=200, unique=True)
    # desc = models.TextField()
    periode = models.IntegerField()
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.membership_type) + '-' + time.strftime("%Y%m%d%H%M%S")
        super(Membership, self).save(*args, **kwargs)

    def __str__(self):
        return self.membership_type


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = ImageField(blank=True, null=True, manual_crop="")
    membership = models.ForeignKey('Membership', related_name='user_membership', on_delete=models.SET_NULL, null=True)
    # is_premium = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]

    @property
    def get_picture_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url


class Subscription(models.Model):
    user_membership = models.ForeignKey(Account, related_name='subscription', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
      return self.user_membership.name
