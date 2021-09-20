from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *



# class Sertificate(models.Model):
#     title = models.CharField(max_length=255, verbose_name='Наименование подарочного сертификата')
#     validity = models.DateField(null=True, blank=True, verbose_name='Срок окончания')
#     amount_value = models.IntegerField(default=0, blank=True, verbose_name='На сумму')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
