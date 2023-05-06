from django.db import models
from django.conf import settings
from utils.validators import validate_extension, validate_size
from django.utils.translation import gettext_lazy as _


# Create your models here.
class ProjectManager(models.Manager):
    def get_related(self):
        return self.select_related('author')

    def get_data_for_home_page(self):
        return self.get_related().only(
            'id',
            'title',
            'photo',
            'description',
            'url',
            'author__first_name',
            'author__last_name'
        )


class Project(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='projects'
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    photo = models.URLField(
        null=True,
        blank=True,
        verbose_name='Фото',
        max_length=250
    )
    date_of_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания проекта'
    )
    url = models.URLField(max_length=250, verbose_name='url Проекта')
    objects = ProjectManager()

    def __str__(self):
        return f'{self.title}: {self.author}'


class Blog(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='blogs'
    )
    date_of_creation = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания записи'
    )
    date_of_updating = models.DateTimeField(
        auto_now=True,
        verbose_name='Время обновления записи'
    )
    location = models.CharField(
        max_length=250,
        verbose_name='Местоположение',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'{self.author}: {self.title}'


# to be considered in the future
class BlogReaction(models.Model):
    LIKED = 'LIKED'
    DISLIKED = 'DISLIKED'

    BLOG_REACTIONS = (
        (LIKED, LIKED),
        (DISLIKED, DISLIKED)
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        verbose_name='Блог',
        related_name='blog_reactions'
    )

    reaction = models.CharField(
        choices=BLOG_REACTIONS,
        null=True,
        blank=True,
        max_length=100
    )

    class Meta:
        verbose_name = _('Реакция на запись')
        verbose_name_plural = _('Реакция на записи')
        unique_together = ('user', 'blog')

    def __str__(self):
        return f'{self.user}, {self.blog}'


# to be considered in the future
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения')
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        verbose_name='Блог'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='blog_comments'
    )

    content = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')

    def __str__(self):
        return f"{self.user}, {self.blog}, {self.content}"
