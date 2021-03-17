from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории статей')
    slug = models.SlugField

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    slug = models.SlugField
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])
    content = models.TextField(verbose_name='Содержание статьи')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата обновлнения')
    publication_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='Категория статьи', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
