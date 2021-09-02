from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import *
from . import views
from .views import *


urlpatterns = [
    path('review/', review, name='review'),
    # path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]