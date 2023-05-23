from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def app(request):
     template = loader.get_template('homepage.html')
     return HttpResponse(template.render())

def chemistry(request):
     chem = loader.get_template('chemistry.html')
     return HttpResponse(chem.render())