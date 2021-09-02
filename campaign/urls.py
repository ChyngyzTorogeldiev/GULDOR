from django.urls import path
from django.conf.urls import url, include
from flowertypes.urls import *
from flowertypes.views import *
from .views import *



urlpatterns = [
    path('', campaign, name='campaign-list')
]