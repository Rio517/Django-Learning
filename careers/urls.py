from django.conf.urls.defaults import *

## CAREERS VIEWS
urlpatterns = patterns('careers.views',
    (r'^$', 'index'),
    (r'^(?P<career_id>\d+)/$', 'show')
)


## JOBS VIEWS
urlpatterns += patterns('careers.views',
    (r'^(?P<career_id>\d+)/jobs/(?P<job_id>\d+)/$', 'show_job'),
    (r'^(?P<career_id>\d+)/jobs/new/$', 'new_job'),
    (r'^(?P<career_id>\d+)/jobs/create/$', 'create_job')
)