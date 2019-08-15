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
    
    
@login_required
def preview_house(request, user_id, house_id):
    """
    View for user to confirm his listing or go back and edit it
    """
    if user_id is not int(request.session['_auth_user_id']):
        return redirect('addhouse', user_id=request.session['_auth_user_id'])

    house_data = get_object_or_404(Listing, pk=int(house_id))
    if house_data.paid_fee:
        messages.error(request, "You already paid for this listing!")
        return redirect('index')

    args = {
        'house': house_data,
        'page_title': house_data.title
    }
    return render(request, "preview_house.html", args)



@login_required
def pay_fee(request, user_id, house_id):
	"""
	View for user to pay fee for new listing
	"""

	if user_id is not int(request.session['_auth_user_id']):
		return redirect('addhouse', user_id=request.session['_auth_user_id'])
	house_data = get_object_or_404(Listing, pk=int(house_id))
	if house_data.paid_fee:
		messages.error(request, "You already paid for this listing!")
		return redirect('index')
	if request.method == "POST":
		payment_form = PayFeeForm(request.POST)
		if payment_form.is_valid():
			try:
				customer = stripe.Charge.create(
					amount=int(1000),
					currency="USD",
					description=request.user.email,
					card=payment_form.cleaned_data['stripe_id'],
				)
			except stripe.error.CardError:
				messages.error(request, "Your card was declined!")

			if customer.paid:
				messages.success(request, "You have successfully paid!")
				messages.success(
					request, "Please note that your listing must be approved by an admin!")       
				if request.session.get('new_house'):
					del request.session['new_house']
				Listing.objects.filter(pk=int(house_id)).update(paid_fee=True)
				args = {
					'house_id': house_data.id
				}
				try:
					user = User.objects.get(pk=int(request.session['_auth_user_id']))
					params = {
						"body": "Thank you",
						"to": [user.email],
						"subject": f"Invoice for {house_data.title}",
						"user": user,
						"house": house_data,
						"template_id": invoice_template_id,
						"invoice_created": datetime.now,                                                
						"file_name": f"{house_data.id}",
					}
					
					Invoice.send_pdf(params)
					messages.success(request, "Invoice has been emailed to you")
					return redirect(reverse("house", kwargs={'house_id': house_data.id}))
				except:
					messages.error(request, "We could not email you invoice...")
					return redirect(reverse("house", kwargs={'house_id': house_data.id}))
			else:
				messages.error(request, "Unable to take payment")

		else:
			messages.error(
				request, "We were unable to take a payment with that card! listing")
	args = {
		'house': house_data,
		'page_title': house_data.title,
		'form': PayFeeForm,
		'publishable': settings.STRIPE_PUBLISHABLE
	}

	return render(request, "pay_fee.html", args)

    
	
def search_by_links(request, key):
    """ 
    Route to let user to search by clicking on links in description
    """

    listings = Listing.objects.all().filter(
        is_published=True).order_by(f'-{key}')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    args = {
        "listings": paged_listings,
        "key": key
    }
    return render(request, "houses.html", args)


def search_by_user(request, user_id):
    """ 
    Route to let user to search by clicking on links in description
    """

    listings = Listing.objects.all().filter(
        is_published=True, seller=user_id).order_by('-list_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    args = {
        "listings": paged_listings
    }
    return render(request, "houses.html", args)

