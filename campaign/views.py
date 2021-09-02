from django.shortcuts import render, HttpResponse
from django.views import View
from flowertypes.models import *
from flowertypes.views import *
from .models import *


def campaign(request):
    campaign_list = RosesBouquet.objects.all()
    campaign_season = SeasonFlowers.objects.all()
    campaign_assorted = AssortedFlowers.objects.all()
    context = {
        'campaign_list': campaign_list,
        'campaign_season': campaign_season,
        'campaign_assorted': campaign_assorted
        }
    return render(request, 'campaign.html', context)



