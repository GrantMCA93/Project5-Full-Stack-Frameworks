from django.shortcuts import render
from django.core.paginator import Paginator
from django import forms
from django.shortcuts import redirect
from django.contrib.auth.models import User

from listings.models import Listing
from enquiries.forms import ContactForm


def index(request):

    return render(request, "index.html")
    
def contact(request):

    return render(request, "contact.html")
    
def contact_thank_you_message(request):
    return render(request, "contact_thank_you_message.html")
    

    
