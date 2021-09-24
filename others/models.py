from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from core.models import Product, Flower
from django.utils import timezone



# class Comment(models.Model):
#     product = models.ForeignKey(Flower,on_delete=models.CASCADE,related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     active = models.BooleanField(default=False)

#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Комментарии {} от {}'.format(self.body, self.name)


# class ProductReview(models.Model):
#     product = models.ForeignKey('ProductReview', Product, related_name='reviews')
#     user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE) 

#     content = models.TextField(blank=True, null=True)
#     stars = models.IntegerField()
#     date_added = models.DateTimeField(auto_now_add=True)

