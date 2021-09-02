from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone



class RosesBouquet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='roses', null=True, blank=True)
    image2 = models.ImageField(upload_to='roses', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)
    

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Букет из роз"
        verbose_name_plural = "Букеты из роз"
        ordering = ['name']



class SeasonFlowers(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='seasonal', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сезонный букет"
        verbose_name_plural = "Сезонные букеты"
        ordering = ['name']


class AssortedFlowers(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='assorted', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ассорти букет"
        verbose_name_plural = "Ассорти букеты"
        ordering = ['name']












