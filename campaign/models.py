from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from flowertypes.models import *


# class Sale(models.Model):
#     created = models.DateTimeField()
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
