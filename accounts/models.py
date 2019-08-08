from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class UserProfile(models.Model):
	""" 
	Model for User (seller)
	"""

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to='main/profile/%Y/%m/%d/', blank=True)
	phone = models.CharField(max_length=15)
	terms = models.BooleanField(default=False)
	joined = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.user.email