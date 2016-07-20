from django.db import models

class Profile(models.Model):
	name 		  	=   models.CharField(max_length = 255, null = False)
	email 			=   models.CharField(max_length = 255, null = False)
	fone 			=	models.CharField(max_length = 15, null = False)
	company_name 	=   models.CharField(max_length = 255, null = False)
	contacts 		=   models.ManyToManyField('self')

	def invite(self, profile_invited):
		invite 		=	Invite(requester = self, guest = profile_invited).save()

class Invite(models.Model):
	requester		=	models.ForeignKey(Profile, related_name='sent')
	guest 			=	models.ForeignKey(Profile, related_name='received')

	def accept(self):
		self.guest.contacts.add(self.requester)
		self.requester.contacts.add(self.guest)
		self.delete()