from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone





class Review(models.Model):
    author = models.CharField(max_length=50)

    # goods = models.ForeignKey(to=RosesBouquets, on_delete=models.CASCADE,
    # verbose_name='Товар')

    text = models.TextField(verbose_name='Отзыв')

    # checked = models.BooleanField(default=False, verbose_name='Обработано')

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
