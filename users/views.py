from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic.base import View
from profiles.models import Profile
from users.forms import UserRegisterForm

# Create your views here.
class UserRegisterView(View):
	template_name = 'register.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = UserRegisterForm(request.POST)

		if form.is_valid():

			form_data = form.data

			user = User.objects.create_user(
				form_data['name'],
				form_data['email'],
				form_data['password'])

			profile = Profile(name = form_data['name'],
							 email = form_data['email'],
							 fone = form_data['fone'],
							 company_name = form_data['company_name'],
							 user = user)
			profile.save()

			return redirect('profileIndex')

		return render(request, self.template_name, {'form' : form})