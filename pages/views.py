from django.shortcuts import render
from django.core.paginator import Paginator
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User

from listings.models import Listing
from enquiries.forms import ContactForm


def index(request):
    """ 
    View for index.html (landing page)
    """
    contact_form = ContactForm()
    listings = Listing.objects.exclude(
        is_published=False).order_by("-list_date")[:3]

    args = {
        "listings": listings,
        "form": contact_form,
        
    }  

    return render(request, "index.html", args)