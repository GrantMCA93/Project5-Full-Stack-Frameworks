from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from listings.models import Listing


class ContactMessage(models.Model):
    """ 
    Model for message from the user
    """

    subject = models.CharField(max_length=50, default="General message")
    your_name = models.CharField(max_length=50, default="Admin")
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=2000)
    posted = models.DateTimeField(default=datetime.now)
    new_message = models.BooleanField(default=True)

    def __str__(self):
        return self.subject


class PropertyEnquire(models.Model):

    """ 
    Model for house enquire message from the user
    """

    to = models.CharField(max_length=100)
    to_id = models.IntegerField(default=1)
    to_email = models.EmailField(max_length=100)
    house_id = models.IntegerField(default=1)
    house_name = models.CharField(max_length=100)
    viewing = models.BooleanField(default=False)
    message = models.TextField(max_length=2000)
    posted = models.DateTimeField(default=datetime.now)
    sender = models.CharField(max_length=100)
    sender_id = models.IntegerField(default=1)
    sender_email = models.EmailField(max_length=100)
    new_to = models.BooleanField(default=True)
    delete_to = models.BooleanField(default=False)
    new_sender = models.BooleanField(default=False)
    delete_sender = models.BooleanField(default=False)

    def __str__(self):
        return self.house_name