from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='profileIndex'),
	url(r'^profiles/(?P<profile_id>\d+)$', views.details, name='profileDetails'),
	url(r'^profiles/(?P<profile_id>\d+)/invite$', views.invite, name='profileInvite'),
	url(r'^profiles/(?P<invite_id>\d+)/accept$', views.accept, name='profileAccept')
)