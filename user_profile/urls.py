from django.conf.urls.defaults import *
import forms
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^profile-settings/$', 'user_profile.views.profile_settings', name='profile_settings'),
    url(r'^register/$', 'registration.views.register', 
        {'backend': 'registration.backends.default.DefaultBackend', 
        'template_name': 'registration/registration.html',
        'form_class': forms.RegistrationForm}, 
        name='registration_register'),
    url(r'^register/complete/$', 'django.views.generic.simple.direct_to_template',
        { 'template': 'registration/registration_complete.html'},
        name='registration_complete'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^logout/$', auth_views.logout,
        {'template_name': 'registration/logout.html'}, name='auth_logout'),
)