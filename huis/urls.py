from django.urls import path

from huis import views


urlpatterns = [
    path('', views.index, name='index'),
    ]