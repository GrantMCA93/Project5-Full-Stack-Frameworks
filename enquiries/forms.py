from django import forms
from .models import ContactMessage, PropertyEnquire


class ContactForm(forms.ModelForm):

	""" 
	Users messages form 
	"""


	subject = forms.CharField(max_length=50)
	your_name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)
	message = forms.CharField(min_length=20, widget=forms.Textarea)

	class Meta:
		model = ContactMessage
		fields = ['subject', 'your_name', 'email', 'message']


class EnquiryForm(forms.ModelForm):

    """ 
    Users Enquiries form 
    """

    message = forms.CharField(min_length=20, widget=forms.Textarea)
    viewing = forms.BooleanField(required=False, label="I am interested to book a viewing")
    new_to = forms.BooleanField(required=False)

    class Meta:
        model = PropertyEnquire
        fields = ['to', 'to_id', 'to_email', 'house_id', 'house_name',
                  'viewing', 'message', 'sender', 'sender_id', 'sender_email', 'new_to']