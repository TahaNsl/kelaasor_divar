from django.urls import path
from ad import views

urlpatterns = [
    path("", views.ads_list, name="ads_list"),
    path("<str:city>/", views.ads_by_city, name="ads_by_city"),
    path("category/<str:category_name>/", views.ads_by_category, name="ads_by_category"),
    path("delete/<str:ad_type>/<int:ad_id>/", views.delete_ad, name="delete_ad"),
]