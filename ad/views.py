from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import CarAd, RealEstateAd, GeneralAd
from category.models import Category



def car_ads_list(request):
    ads = CarAd.objects.all().values()
    return JsonResponse(list(ads), safe=False)

def realestate_ads_list(request):
    ads = RealEstateAd.objects.all().values()
    return JsonResponse(list(ads), safe=False)

def general_ads_list(request):
    ads = GeneralAd.objects.all().values()
    return JsonResponse(list(ads), safe=False)

def ads_list(request):
    car_ads = list(CarAd.objects.all().values())
    for ad in car_ads:
        ad["type"] = "car"

    realestate_ads = list(RealEstateAd.objects.all().values())
    for ad in realestate_ads:
        ad["type"] = "realestate"

    general_ads = list(GeneralAd.objects.all().values())
    for ad in general_ads:
        ad["type"] = "general"

    all_ads = car_ads + realestate_ads + general_ads
    return JsonResponse(all_ads, safe=False)

def ads_by_city(request, city):
    car_ads = list(CarAd.objects.filter(city__iexact=city).values())
    for ad in car_ads:
        ad["type"] = "car"

    realestate_ads = list(RealEstateAd.objects.filter(city__iexact=city).values())
    for ad in realestate_ads:
        ad["type"] = "realestate"

    general_ads = list(GeneralAd.objects.filter(city__iexact=city).values())
    for ad in general_ads:
        ad["type"] = "general"

    return JsonResponse(car_ads + realestate_ads + general_ads, safe=False)

def ads_by_category(request, category_name):
    category = get_object_or_404(Category, name__iexact=category_name)

    car_ads = list(CarAd.objects.filter(category=category).values())
    for ad in car_ads:
        ad["type"] = "car"

    realestate_ads = list(RealEstateAd.objects.filter(category=category).values())
    for ad in realestate_ads:
        ad["type"] = "realestate"

    general_ads = list(GeneralAd.objects.filter(category=category).values())
    for ad in general_ads:
        ad["type"] = "general"

    return JsonResponse(car_ads + realestate_ads + general_ads, safe=False)

def delete_ad(request, ad_type, ad_id):
    model_map = {
        "car": CarAd,
        "realestate": RealEstateAd,
        "general": GeneralAd,
    }

    Model = model_map.get(ad_type)
    if not Model:
        return JsonResponse({"error": "Invalid ad type."}, status=400)

    ad = get_object_or_404(Model, id=ad_id)
    ad.delete()
    return JsonResponse({"message": f"{ad_type} ad {ad_id} deleted successfully."})