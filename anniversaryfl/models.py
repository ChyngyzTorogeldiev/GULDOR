from django.db import models
from django.contrib import admin 
from django.contrib.auth.models import User



class HundredRoseFlowers(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='hundredroses', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)
    

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "101 роза"
        verbose_name_plural = 'Букеты из 101 роз'
        ordering = ['name']




class WeddingBouquetFlowers(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='wedding', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)
    

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Свадебный букет"
        verbose_name_plural = 'Свадебные букеты'
        ordering = ['name']


class BasketBouquetFlowers(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='basketflower', null=True, blank=True)
    sale = models.IntegerField('Discount percentage', null=True, blank=True, default=0)
    

    def get_sale(self):
        price = int(self.price * (100 - self.sale) / 100)
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Букет в корзинке"
        verbose_name_plural = 'Букеты в корзинках'
        ordering = ['name']


