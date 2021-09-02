from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *


# Flowers in pots category


def flowers_in_pots(request):
    flowersinpots_object = FlowersinPots.objects.all()
    return render(request, 'flowersinpots/flowers.html',
    {'flowersinpots': flowersinpots_object})

def flowerinpot(request, id):
    try:
        flowerinpot_object = FlowersinPots.objects.get(id=id)
        return render(request, 'flowersinpots/flowersinpots.html', {
        'flowerinpot_object': flowerinpot_object
        })
    except FlowersinPots.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)


## Home plants

def home_plants(request):
    homeplants_object = HomePlants.objects.all()
    return render(request, 'homeplants/flowers.html',
    {'homeplants': homeplants_object})

def homeplant(request, id):
    try:
        homeplant_object = HomePlants.objects.get(id=id)
        return render(request, 'homeplants/homeplant.html', {
        'homeplant_object': homeplant_object
        })
    except HomePlants.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)



## Decorative plants

def decor_plants(request):
    decorplants_object = DecorPlants.objects.all()
    return render(request, 'decorplants/flowers.html',
    {'decorplants': decorplants_object})

def decor(request, id):
    try:
        decor_object = DecorPlants.objects.get(id=id)
        return render(request, 'decorplants/decor.html', {
        'decor_object': decor_object
        })
    except DecorPlants.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)