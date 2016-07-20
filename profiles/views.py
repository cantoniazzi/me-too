from django.shortcuts import render, redirect
from profiles.models import Profile, Invite

def index(request):
	return render(request, 'index.html',{'profiles' : Profile.objects.all(), 'profile_logged' : get_profile_logged(request)})

def details(request, profile_id):
	profile = Profile.objects.get(id = profile_id)
	profile_logged = get_profile_logged(request)
	is_contact = profile in profile_logged.contacts.all()

	return render(request,'details.html', {'profile' : profile, 
										   'profile_logged' : get_profile_logged(request),
										   'is_contact': is_contact})

def invite(request, profile_id):
	profile_to_invite = Profile.objects.get(id=profile_id)
	profile_logged = get_profile_logged(request)
	profile_logged.invite(profile_to_invite)
	return redirect('profileIndex')

def get_profile_logged(request):
	return Profile.objects.get(id=1)

def accept(request, invite_id):
	invite = Invite.objects.get(id=invite_id)
	invite.accept()
	return redirect('profileIndex')