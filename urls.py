from django.conf.urls.defaults import *
from django.contrib import admin
import user_profile
from registration.views import activate
from django.contrib.auth import views as auth_views

admin.autodiscover()
handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('user_profile.urls')),
    url(r'^training/', include('muscle.urls')),
    url(r'^activate/(?P<activation_key>\w+)/$', activate,
       { 'backend': 'registration.backends.default.DefaultBackend' },
       name='registration_activate'),
    url('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
)   
