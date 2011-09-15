from django.db import models
from django.forms import ModelForm
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.extras.widgets import SelectDateWidget


#I decided to skip career_fields for now.

#class Field(models.Model):
#  name = models.CharField(max_length=150) 
#  description_short = models.CharField(max_length=255) 
#  description_long = models.TextField()

class Career(models.Model):
  #field = models.ForeignKey(Field)
  name = models.CharField(max_length=150) 
  description_short = models.CharField(max_length=255) 
  description_long = models.TextField()

# Jobs within a career
class Job(models.Model): 
  title = models.CharField(max_length=150) 
  career = models.ForeignKey(Career)

  description_short = models.CharField(max_length=255) 
  description_long = models.TextField()
  prerequisets = models.TextField()
  #created_at = models.DateField(null=True, blank=True)
  
  def __unicode__(self):
    return self.title


#invidiual entries of having had xyz job
class Entry(models.Model):
  job = models.ForeignKey(Job)
  #at a later date we'd want to track career paths via users, besides having a 
  #user = models.ForeignKey(User)
  salary = models.IntegerField()
  started_at = models.DateField(null=True, blank=True)
  ended_at = models.DateField(null=True, blank=True)
  comment = models.TextField(null=True, blank=True)
  preceding = models.ForeignKey(Job, related_name="preceding_job", null=True, blank=True)
  following = models.ForeignKey(Job, related_name="following_job", null=True, blank=True)
  
class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('salary', 'started_at', 'ended_at', 'comment', 'preceding', 'following')
        widgets = {
            'started_at': SelectDateWidget(),
            'ended_at': SelectDateWidget(),
        }
        