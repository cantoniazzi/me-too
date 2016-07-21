from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.Form):
	name      	 = forms.CharField(required = True)
	email     	 = forms.CharField(required = True)
	password  	 = forms.CharField(required = True)
	fone         = forms.CharField(required = True)
	company_name = forms.CharField(required = True)

	def is_valid(self):
		valid = True
		if not super(UserRegisterForm, self).is_valid():
			self.add_errorForm("Please, check the informed data")
			valid = False

		user_exists = User.objects.filter(username=self.data['name']).exists()
		
		if user_exists:
			self.add_errorForm("User already exists")
			valid = False
		
		return valid

	def add_errorForm(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,forms.utils.ErrorList())
		errors.append(message)