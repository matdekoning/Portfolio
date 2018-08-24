from django.urls import path

from image import views

urlpatterns = [
    path('', views.index, name='index'),
    path('go', views.changed, name='changed'),
    ]