# April 18, 2020
# Kyle Ear
# Gerardo Pena
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import Account

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

	class Meta:
		model = Account
		fields = ("email","username","password1","password2")

class AccountUpdateForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = (
			'email',
			'username',
			'first_name',
			'last_name',
			'street_address',
			'city_address',
			'state_address',
			'zip_address'
			)

	def clean_email(self):
		# check if email is available
		if self.is_valid():
			email = self.cleaned_data['email']
			# check if account exists
			try:
				account = Account.object.exclude(pk=self.instance.pk).get(email=email)
			except Account.DoesNotExist:
				return email
			raise forms.ValidationError('Email "%s" is already in use.' % account.email)

	def clean_username(self):
		# check if email is available
		if self.is_valid():
			username = self.cleaned_data['username']
			try:
				account = Account.object.exclude(pk=self.instance.pk).get(username=username)
			except Account.DoesNotExist:
				return username
			raise forms.ValidationError('Username "%s" is already in use.' % account.username)

	def clean_first_name(self):
		if self.is_valid():
			first_name = self.cleaned_data['first_name']
			return first_name

	def clean_last_name(self):
		if self.is_valid():
			last_name = self.cleaned_data['last_name']
			return last_name

	def clean_street_address(self):
		if self.is_valid():
			street_address = self.cleaned_data['street_address']
			return street_address

	def clean_city_address(self):
		if self.is_valid():
			city_address = self.cleaned_data['city_address']
			return city_address

	def clean_state_address(self):
		if self.is_valid():
			state_address = self.cleaned_data['state_address']
			return state_address

	def clean_zip_address(self):
		if self.is_valid():
			zip_address = self.cleaned_data['zip_address']
			return zip_address
