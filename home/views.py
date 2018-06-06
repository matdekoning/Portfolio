from django.shortcuts import render
from django.http import HttpResponse
from .forms import HomeForm, TwitterForm, UploadImage
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    homeform = HomeForm()
    twitter = TwitterForm()
    upload = UploadImage()
    return render(request, 'index.html', {'homeform':homeform, 'twitter':twitter, 'upload':upload})
