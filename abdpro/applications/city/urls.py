from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "city_app"

urlpatterns = [
        path('NewCity/',
                views.CityAPISerializer.as_view(),
                name='NewCity'),
]