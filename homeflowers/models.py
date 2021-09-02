from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone


class FlowersinPots(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='homeflowers', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)
    

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цветы в горшках"
        verbose_name_plural = "Цветы в горшках"
        ordering = ['name']


class HomePlants(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='homeflowers', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)
    

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комнатное растение"
        verbose_name_plural = "Комнатные растения"
        ordering = ['name']



class DecorPlants(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='homeflowers', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)
    

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Декоративное растение"
        verbose_name_plural = "Декоративные растения"
        ordering = ['name']