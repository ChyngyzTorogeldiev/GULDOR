from django.shortcuts import render
from .models import *

## 101 rose bouquets

def hundredrose_bouquets(request):
    hundredbouquets_object = HundredRoseFlowers.objects.all()
    return render(request, 'hundredrose/anniversary1.html', 
    {'hundredroses': hundredbouquets_object})


def hundredrose(request, id):
    try:
        hundredrose_object = HundredRoseFlowers.objects.get(id=id)
        return render(request, 'hundredrose/hundredrose.html',
        {'hundredrose_object': hundredrose_object})
    except HundredRoseFlowers.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)



## Wedding bouquets functions

def weddingbouquets(request):
    weddingbouquets_object = WeddingBouquetFlowers.objects.all()
    return render(request, 'wedding/anniversary2.html', 
    {'weddingbouquets': weddingbouquets_object})


def weddingflower(request, id):
    try:
        wedding_object = WeddingBouquetFlowers.objects.get(id=id)
        return render(request, 'wedding/wedding.html',
        {'wedding_object': wedding_object})
    except WeddingBouquetFlowers.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)


## basket flowers

def basketbouquets(request):
    basketbouquet_object = BasketBouquetFlowers.objects.all()
    return render(request, 'basketfl/anniversary3.html', 
    {'basketbouquets': basketbouquet_object})


def basketflower(request, id):
    try:
        basketfl_object = BasketBouquetFlowers.objects.get(id=id)
        return render(request, 'basketfl/basketflowers.html',
        {'basketfl_object': basketfl_object})
    except BasketBouquetFlowers.DoesNotExist as e:
        return HttpResponse(f'Товар не существует: {e}', status=404)

