from django.shortcuts import render_to_response, get_object_or_404
from careers.models import Career, Job, Entry
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
  careers_list = Career.objects.all()
  return render_to_response('index.html', {'careers_list': careers_list})


def show(request, career_id):
  career = get_object_or_404(Career, pk=career_id)
  return render_to_response('show.html', {'career': career})
  
def show_job(request, career_id, job_id):
  job = get_object_or_404(Job, pk=job_id)
  return render_to_response('show_job.html', {'job': job, 'career_id': career_id})
  
def new_job(request, career_id):
  return HttpResponse("Placeholder for a new job in career_id: %s." % career_id)
  