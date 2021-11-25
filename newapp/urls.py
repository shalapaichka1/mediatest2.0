from .views import *
from django.urls import path


urlpatterns = [
    path('city/', api_city),
    path('city//street/<int:city_id>/', api_city_street),
    path('shop/', api_shop),
]
