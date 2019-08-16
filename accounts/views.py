from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.conf import settings
from django.core.paginator import Paginator
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import UserProfileForm, UserLoginForm, EditProfileForm, EditUserForm
from enquiries.forms import EnquiryForm
from listings.models import Listing
from listings.forms import AddListingForm, PayFeeForm, EditListingForm
import stripe

stripe.api_key = settings.STRIPE_SECRET

@login_required
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('index')


def login(request):
    if request.user.is_authenticated:
        messages.error(request, "You are already logged in!")
        return redirect('index')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in!")
                nexturl = request.POST.get('next')
                if nexturl:
                    return redirect(nexturl)
                else:
                    return redirect('profile')
            else:
                form.add_error(
                    None, "Your username and password is incorrect!")

                return render(request, "login.html", {'form': form})
        else:
            messages.error(request, form.errors)
            return render(request, "login.html", {'form': form})
    else:
        form = UserLoginForm()
    return render(request, "login.html", {'form': form})


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')





def register(request):
    """A view that manages the registration form"""
    if request.user.is_authenticated:
        messages.error(request, "You are registered and logged in already!")
        return redirect('index')
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))
            
            profile = UserProfile(
                user=user,
                img=request.POST.get('img'),
                phone=request.POST.get('phone'),
                description=request.POST.get('description'),
                terms=True,
            )
            profile.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('profile')

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserProfileForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
    
    
    """
    listings views.py
    """    


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
    # Automaticaly autofill fields if house exist in session
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
def edit_profile(request):
    """
    View to let user to edit his profile data
    """
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(
            request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.userprofile)
    args = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "edit_profile.html", args)