from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import sqlite3
import Cloudstack.CloudStack.Client
from vmm.models import Vm

# Create your views here.


def login(request):
	return render_to_response("login.html")

def dictfetchall(cursor):
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def showUsers(request):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()
	c.execute("SELECT * FROM person_user where role='simpleuser' ;")
	rows = dictfetchall(c)
	return render_to_response("all-users.html",{'users':rows,'role':request.session["role"],'username':request.session["username"]})

def logout(request):
	request.session["role"] = False
	request.session["username"] = False
	return  HttpResponseRedirect("/login")

def createAccount(request):
	return render_to_response("create-account.html")

def createAccountLogic(request):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()
	c.execute("insert into person_user values (NULL,'"+request.POST['username']+"','"+request.POST['password']+"','simpleuser','"+request.POST['gender']+"');");
	conn.commit()
	return  HttpResponseRedirect("/login")

def verification(request):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()
	c.execute("SELECT username,password,role FROM person_user where username ='"+request.POST['username']+"' and password='"+request.POST['password']+"';");
	conn.commit()
	
	username,password,role, = c.fetchone()
	
	if username == request.POST['username'] and password == request.POST['password']:
		request.session["username"] = username
		request.session["role"] = role
		return  HttpResponseRedirect("/allVms")
	else:
		return  HttpResponseRedirect("/login")
	
