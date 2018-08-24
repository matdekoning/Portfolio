from django.shortcuts import render
from django.http import HttpResponse
from .forms import HomeForm, TwitterForm, UploadImage
from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
# Create your views here.

def index(request):
    homeform = HomeForm()
    twitter = TwitterForm()
    upload = UploadImage(request.POST or None, request.FILES or None)
    return render(request, 'index.html', {'homeform':homeform, 'twitter':twitter, 'upload':upload})



