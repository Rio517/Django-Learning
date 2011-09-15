from django.shortcuts import render_to_response, get_object_or_404
from careers.models import Career, Job, Entry, EntryForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf



def index(request):
  careers_list = Career.objects.all()
  return render_to_response('index.html', {'careers_list': careers_list})


def career_show(request, career_id):
  career = get_object_or_404(Career, pk=career_id)
  return render_to_response('career_show.html', {'career': career})
  
def job_show(request, career_id, job_id):
  job = get_object_or_404(Job, pk=job_id)
  return render_to_response('job_show.html', {'job': job, 'career_id': career_id})
  
def entry_new(request, career_id, job_id):
  formset = EntryForm()
  return render_to_response('entry_new.html', {'formset': formset, 'career_id': career_id, 'job_id': job_id}, context_instance=RequestContext(request))
  
def entry_create(request, career_id, job_id):
  job_loaded = Entry(job_id = job_id)
  formset = EntryForm(data=request.POST, instance=job_loaded)
  if formset.is_valid():
    formset.save()
    return HttpResponseRedirect('/careers/' + career_id + '/jobs/' + job_id)
  else:
    return render_to_response('entry_new.html', {'formset': formset, 'career_id': career_id, 'job_id': job_id}, context_instance=RequestContext(request))
    