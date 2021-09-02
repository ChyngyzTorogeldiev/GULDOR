from django.urls import path
from django.conf.urls import url, include
from flowertypes.models import *
from .models import *
from . import views
from .views import *



urlpatterns = [
    path('rosesbouquet', roses_bouquets, name='roses-bouquet'),
    path('rosesbouquet/<int:id>/', rose, name='rose'),
    path('seasonal', season_bouquets, name='season-bouquets'),
    path('seasonal/<int:id>/', season, name='season'),
    path('assorted', assorted_bouquets, name='assorted-bouquets'),
    path('assorted/<int:id>/', assorted, name='assorted'),
]