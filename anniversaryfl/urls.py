from django.urls import path
from .views import *


urlpatterns = [
    path('hundredroses', hundredrose_bouquets, name='hundredrose-bouquets'),
    path('hundredroses/<int:id>/', hundredrose, name='hundredrose'),
    path('weddingbouquets', weddingbouquets, name='wedding-bouquets'),
    path('weddingbouquets/<int:id>/', weddingflower, name='weddingflower'),
    path('basketbouquets', basketbouquets, name='basket-bouquets'),
    path('basketbouquets/<int:id>/', basketflower, name='basketflower'),
]