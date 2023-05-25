from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def app(request):
     template = loader.get_template('homepage.html')
     return HttpResponse(template.render())

def biology(request):
     bio = loader.get_template('biology.html')
     return HttpResponse(bio.render())

def chemistry(request):
     chem = loader.get_template('chemistry.html')
     return HttpResponse(chem.render())

def geography(request):
     chem = loader.get_template('geography.html')
     return HttpResponse(chem.render())

def mathematics(request):
     chem = loader.get_template('mathematics.html')
     return HttpResponse(chem.render())