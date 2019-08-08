from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, reverse
from django.contrib import messages, auth
from django.template.context_processors import csrf
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import stripe
from listings.models import Listing
from listings.forms import AddListingForm, PayFeeForm, EditListingForm
from enquiries.forms import EnquiryForm
from.invoice import Invoice


def listings(request):
    """A view that displays the listings page of a logged in user"""
    return render(request, 'listings.html')


def house(request, house_id):
    """
    Main route for a single house
    """
    house_data = get_object_or_404(Listing, pk=house_id)

    args = {
        'house': house_data,
        'page_title': house_data.title,
        'form': EnquiryForm
    }
    return render(request, "house.html", args)


def houses(request):
    """
            Main route for all houses
            """
    listings = Listing.objects.all().filter(
        is_published=True).order_by('-list_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')

    return render(request, "houses.html")






@login_required
def addhouse(request, user_id):
    """
    Main route for adding new house listing
    """

    if request.session.get('new_house'):
        zipcode = request.session['new_house']['zipcode'].lower()
        zipcode = zipcode.replace(" ", "")
        Listing.objects.filter(zipcode=zipcode).delete()
    # Check if user want to add listing under different id
    if user_id is not int(request.session['_auth_user_id']):
        return redirect('addhouse', user_id=request.session['_auth_user_id'])
    if request.method == 'POST':
        form = AddListingForm(request.POST, request.FILES)
        if form.is_valid():
            new_house = form.save(commit=False)
            new_house.save()
            # Store houses to session
            request.session['new_house'] = form.data
            return redirect("preview_house", user_id=user_id, house_id=new_house.id)
        else:
            messages.error(request, "Please correct the error/s to proceed!")
            return render(request, "addhouse.html", {'form': form})
    # Automaticaly autofill feilds if house exist in session
    if request.session.get('new_house'):
        listing_form = AddListingForm(request.session['new_house'])
    else:
        listing_form = AddListingForm(initial={
            "price": 0,
            "square_feet": 500,
            "bedrooms": 0,
            "bathrooms": 0,
            "garage": 0,
        })

    args = {
        "form": listing_form
    }
    return render(request, "addhouse.html", args)
