from django.urls import path

from contact import views
from django.contrib import admin


urlpatterns = [

    path('', views.index, name='index'),
    ]