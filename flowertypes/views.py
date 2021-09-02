from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *


# Roses category


def roses_bouquets(request):
    roses_bouquets_object = RosesBouquet.objects.all()
    return render(request, 'roses/flowers.html',
    {'rosesbouquet': roses_bouquets_object})

def rose(request, id):
    try:
        roses_object = RosesBouquet.objects.get(id=id)
        return render(request, 'roses/roses.html', {
        'roses_object': roses_object
        })
    except RosesBouquet.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)


# # Seasonal category      

def season_bouquets(request):
    season_bouquets_object = SeasonFlowers.objects.all()
    return render(request, 'seasonal/seasonalflowers.html',
    {"seasonbouquets": season_bouquets_object})

def season(request, id):
    try:
        season_object = SeasonFlowers.objects.get(id=id)
        return render(request, 'seasonal/season.html',
        {'season_object': season_object})
    
    except SeasonFlowers.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)


# # Assorted bouquets 

def assorted_bouquets(request):
    assorted_bouquets_object = AssortedFlowers.objects.all()
    return render(request, 'assorted/assortedflowers.html',
    {"assortedbouquets": assorted_bouquets_object})
    

def assorted(request, id):
    try:
        assorted_object = AssortedFlowers.objects.get(id=id)
        return render(request, 'assorted/assorted.html',
        {'assorted_object': assorted_object})
    
    except AssortedFlowers.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)






