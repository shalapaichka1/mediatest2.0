from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import *
from datetime import datetime


@api_view(['GET'])
def api_city(request):
    # Пункт A
    if request.method == 'GET':
        city = City.objects.all()
        serializer = CitySerializers(city, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(status=400)


@api_view(['GET'])
def api_city_street(request, city_id):
    # Пункт B
    if request.method == 'GET':
        street = Street.objects.filter(pk=city_id)
        serializer = StreetSerializers(street, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(status=400)


@api_view(['GET', 'POST'])
def api_shop(request):
    # Пункт C
    if request.method == 'POST':
        data = dict(request.POST)
        shop = Shop.objects.create(name=data['name'][0], house_number=data['house_number'][0],
                                   openTime=data['openTime'][0], closeTime=data['closeTime'][0],
                                   city_id=data['city_id'][0], street_id=data['street_id'][0])
        serializer = ShopCreateSerializers(shop)
        return JsonResponse(serializer.data, safe=False, status=200)
    # Пункт D
    elif request.method == 'GET':
        street = request.GET.get("street", "")
        city = request.GET.get("city", "")
        open = request.GET.get("open", "") == "1"
        if open:
            d = datetime.time(datetime.now())
            shops = Shop.objects.filter(openTime__gte=d, closeTime__lt=d) \
                .filter(city__name=city).filter(street__name=street)
            serializer = ShopSerializers(shops, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
        else:
            d = datetime.time(datetime.now())
            shops = Shop.objects.exclude(openTime__gte=d, closeTime__lt=d) \
                .filter(city__name=city).filter(street__name=street)
            serializer = ShopSerializers(shops, many=True)
            return JsonResponse(serializer.data, safe=False, status=200)
    else:
        return JsonResponse(status=400)
