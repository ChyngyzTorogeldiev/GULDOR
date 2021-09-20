from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *


def campaign(request):
    return render(request, 'campaign.html')



