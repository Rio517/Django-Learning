from django.conf.urls.defaults import *

## CAREERS VIEWS
urlpatterns = patterns('careers.views',
    (r'^$', 'index'),
    (r'^(?P<career_id>\d+)/$', 'career_show')
)


## JOBS VIEWS
urlpatterns += patterns('careers.views',
    (r'^(?P<career_id>\d+)/jobs/(?P<job_id>\d+)/$', 'job_show')
)


#ENTRY VIEWS
urlpatterns += patterns('careers.views',
    (r'^(?P<career_id>\d+)/jobs/(?P<job_id>\d+)/entries/new/$', 'entry_new'),
    (r'^(?P<career_id>\d+)/jobs/(?P<job_id>\d+)/entries/create/$', 'entry_create')
)