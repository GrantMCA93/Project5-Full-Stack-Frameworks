from django import forms


class ContactForm(forms.ModelForm):

	""" 
	Users messages form 
	"""


	subject = forms.CharField(max_length=50)
	your_name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)
	message = forms.CharField(min_length=15, widget=forms.Textarea)



class EnquiryForm(forms.ModelForm):

    """ 
    Users Enquiries form 
    """

    message = forms.CharField(min_length=15, widget=forms.Textarea)
    viewing = forms.BooleanField(required=False, label="I am interested to book a viewing")
    new_to = forms.BooleanField(required=False)

   