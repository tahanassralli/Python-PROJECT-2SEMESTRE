from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
#from django.core.context_precessors import csrf

import sqlite3

from template.models import Template
from vmm.models import Vm

# Create your views here.

def ListTemplateView(request):
	return render_to_response('list-template.html',{'templates':Template.objects.all()})

def createTemplate(request):
	username = request.session["username"]
	return render_to_response('create-template.html',{'username':username})

def createTemplateLogic(request):
	return render_to_response('list-template.html')


