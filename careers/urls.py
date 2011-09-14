from django.conf.urls.defaults import *

## CAREERS VIEWS
urlpatterns = patterns('careers.views',
    (r'^$', 'index'),
    (r'^(?P<career_id>\d+)/$', 'show')
)


## JOBS VIEWS
urlpatterns += patterns('careers.views',
    #(r'^careers/(?P<career_id>\d+)/jobs/(?P<job_id>\d+)/$', 'show'),
    (r'^(?P<career_id>\d+)/jobs/new/$', 'new'),
    (r'^(?P<career_id>\d+)/jobs/create/$', 'create')
)