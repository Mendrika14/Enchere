from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render({}, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  return HttpResponseRedirect(reverse('index'))