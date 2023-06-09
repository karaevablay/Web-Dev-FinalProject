from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class MainUserManager(BaseUserManager):
    use_in_migrations = True

    def get_all_users(self):
        return self.select_related('profile')

    def get_user_with_blogs(self):
        return self.prefetch_related('blogs').filter(is_superuser=False, is_staff=False)

    def get_user_data_for_home_page(self):
        return self.get_all_users().only(
            'id',
            'first_name',
            'last_name',
            'photo',
            'profile__brief_description'
        )

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class MainUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    photo = models.URLField(max_length=150, verbose_name='Фото')

    objects = MainUserManager()

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Profile(models.Model):
    brief_description = models.TextField(max_length=500, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    location = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Местоположение'
    )
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE,
                                related_name='profile')  # To get access through Person.profile
    place_of_study = models.CharField(max_length=100, blank=True, null=True, verbose_name='Место обучения')
    course = models.IntegerField(verbose_name='Курс', default=2, blank=True, null=True)
    hobbies = ArrayField(models.CharField(max_length=50), null=True, blank=True)
    skills = ArrayField(models.CharField(max_length=50), null=True, blank=True)

    def __str__(self):
        return f'Profile {self.id}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
