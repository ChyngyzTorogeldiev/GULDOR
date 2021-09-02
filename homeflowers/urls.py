from django.urls import path
from .views import *


urlpatterns = [
    path('flowersinpots', flowers_in_pots, name='flowers-inpots'),
    path('flowersinpots/<int:id>/', flowerinpot, name='flowerinpot'),
    path('homeplants', home_plants, name='home-plants'),
    path('homeplants/<int:id>/', homeplant, name='homeplant'),
    path('decorative', decor_plants, name='decor-plants'),
    path('decorative/<int:id>/', decor, name='decor'),
]