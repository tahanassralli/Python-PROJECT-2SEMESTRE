from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
#from django.core.context_precessors import csrf

import sqlite3

from vmm.models import Vm

from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic.base import TemplateView

conn = sqlite3.connect('testDB')
c = conn.cursor()

# Create your views here.


def getVmById(request,vm_id):
	return render_to_response('vm.html',{'vm':Vm.objects.get(id=vm_id),'role':request.session["role"],'username':request.session["username"]})

def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def log(request):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()
	c.execute("SELECT * FROM log_event ;")
	rows = dictfetchall(c)
	conn.close()
	#return HttpResponse(len(rows))
	return render_to_response('log.html',{'events':rows,'role':request.session["role"],'username':request.session["username"]})

def deleteevent(request,eventid):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()
	c.execute("Delete FROM log_event where id="+eventid+" ;")
	conn.commit()
	c.execute("SELECT * FROM log_event ;")
	conn.commit()
	rows = dictfetchall(c)
	conn.close()
	return HttpResponseRedirect("/log")


def CreateVmView(request):
	return render_to_response('edit_Vm.html',{'role':request.session["role"],'username':request.session["username"]})


