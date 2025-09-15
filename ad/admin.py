from django.contrib import admin
from .models import CarAd, RealEstateAd, GeneralAd



class CarAdAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "city", "price", "make", "model", "gearbox", "created_at")
    list_filter = ("city", "make", "gearbox", "condition")
    search_fields = ("title", "description", "make", "model")


class RealEstateAdAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "city", "price", "estate_type", "transaction_type", "rooms", "area", "created_at")
    list_filter = ("city", "estate_type", "transaction_type")
    search_fields = ("title", "description", "estate_type")


class GeneralAdAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "city", "price", "brand", "condition", "created_at")
    list_filter = ("city", "brand", "condition")
    search_fields = ("title", "description", "brand")


admin.site.register(CarAd, CarAdAdmin)
admin.site.register(RealEstateAd, RealEstateAdAdmin)
admin.site.register(GeneralAd, GeneralAdAdmin)