from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def corses(request):
  template = loader.get_template('ss.html')
  return HttpResponse(template.render())