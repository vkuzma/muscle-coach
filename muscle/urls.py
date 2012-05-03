from django.conf.urls.defaults import *
urlpatterns = patterns('',
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/add/$', 'muscle.views.add', name='add'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/detail/$', 'muscle.views.detail', name='detail'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', 'muscle.views.overview_month', name='overview_month'),
    url(r'^config/$', 'muscle.views.config', name='config'),
    url(r'^config/add-training/$', 'muscle.views.add_training', name='add_trainig'),
    url(r'^$', 'muscle.views.overview', name='overview'),
)