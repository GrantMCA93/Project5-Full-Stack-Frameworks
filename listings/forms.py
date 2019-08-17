from django import forms
from .models import Listing


class AddListingForm(forms.ModelForm):
    """ 
    Form to create new listing 
    """

    bedrooms = forms.IntegerField(min_value=0, max_value=10)
    bathrooms = forms.IntegerField(min_value=0, max_value=5)
    garage = forms.IntegerField(min_value=0, max_value=5)
    bedrooms = forms.IntegerField(min_value=0, max_value=10)
    square_feet = forms.IntegerField(min_value=500)

    class Meta:
        model = Listing
        fields = ['title', 'address', 'city', 'zipcode', 'description', 'price', 'bedrooms',
                  'bathrooms', 'garage', 'square_feet', 'main_img', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'seller']

    def clean_zipcode(self):
        zipcode = self.cleaned_data.get('zipcode').lower()
        zipcode = zipcode.replace(" ", "")
        if Listing.objects.filter(zipcode=zipcode):
            raise forms.ValidationError(
                "zipcode of the property must be unique")
        return zipcode

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if int(price) <= 0:
            raise forms.ValidationError(
                "Price must be greater than 0")
        return price

    def clean_bedrooms(self):
        bedrooms = self.cleaned_data.get('bedrooms')
        if int(bedrooms) <= 0:
            raise forms.ValidationError(
                "Your house must have at least 1 bedroom")
        return bedrooms


class PayFeeForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2019, 2036)]

    credit_card_number = forms.IntegerField(
        label='Card number', required=False)
    cvv = forms.IntegerField(label='CVV', required=False)
    expiry_month = forms.ChoiceField(
        label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)

   

class EditListingForm(forms.ModelForm):
    """
    Form to edit existing listing in databse
    """

    bedrooms = forms.IntegerField(min_value=0, max_value=10)
    bathrooms = forms.IntegerField(min_value=0, max_value=5)
    garage = forms.IntegerField(min_value=0, max_value=5)
    bedrooms = forms.IntegerField(min_value=0, max_value=10)
    main_img = forms.ImageField(required=False)

    class Meta:
        model = Listing
        fields = ['title', 'address', 'city', 'zipcode', 'description', 'price', 'bedrooms',
                  'bathrooms', 'garage', 'square_feet', 'main_img', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'seller']