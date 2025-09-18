from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class AdBase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=0, null=True, blank=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class CarAd(AdBase):
    make = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    condition = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        choices=[
            ("new", "نو"),
            ("like_new", "در حد نو"),
            ("used", "کارکرده"),
            ("damaged", "تصادفی"),
        ],
    )
    gearbox = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=[
            ("automatic", "اتوماتیک"),
            ("manual", "دنده‌ای"),
        ],
    )

    insurance_months_left = models.IntegerField(null=True, blank=True)
    is_accident = models.BooleanField(default=False)

    fuel_type = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=[
            ("gasoline", "بنزینی"),
            ("diesel", "دیزلی"),
            ("hybrid", "هیبریدی"),
            ("electric", "برقی"),
        ],
    )

    def __str__(self):
        return f"{self.make} {self.model} - {self.city}"


class RealEstateAd(AdBase):
    estate_type = models.CharField(max_length=100, blank=True, null=True)
    transaction_type = models.CharField(max_length=50, blank=True, null=True)
    area = models.FloatField(null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)
    floor = models.CharField(max_length=50, blank=True, null=True)
    has_parking = models.BooleanField(default=False)
    has_elevator = models.BooleanField(default=False)
    year_built = models.IntegerField(null=True, blank=True)
    has_deed = models.BooleanField(default=False)
    deed_type = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.city}"


class GeneralAd(AdBase):
    brand = models.CharField(max_length=100, blank=True, null=True)
    warranty = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.city}"