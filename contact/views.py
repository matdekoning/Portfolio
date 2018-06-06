from django.shortcuts import render, redirect, HttpResponse
from contact.forms import ContactForm


# Create your views here.
def index(request):
    form_class = ContactForm
    if request.method == 'GET':

        thankYou = 'Contact us:'
    else:
        thankYou = 'Thank you, your message has been send!'
    return render(request, 'contact.html', {'form': form_class, 'thankYou': thankYou})

