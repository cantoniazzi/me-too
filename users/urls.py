from django.conf.urls import patterns, url
from views import UserRegisterView

urlpatterns = patterns('',
	url(r'^register/$',UserRegisterView.as_view(), name ='register'),
	url(r'^login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}, name='login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',{'login_url':'/login/'}, name='logout')
)