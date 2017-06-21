import CloudStack
from django.shortcuts import render_to_response
from sys import argv
import datetime
import sqlite3
from django.http import HttpResponse,HttpResponseRedirect
from vmm.models import Vm




	

def creationTemplate(displaytext,name,ostypeid,volumeid):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()	
	api = 'http://196.203.216.18:5555/client/api'
	apikey = '3U7UPLR4JHYEzOhKe0JYnR_ICChdmuynnl0SdqmFzFgG4Hgd6BJHHjcSk2K3SsXUvheLEoN-SlRuEOpqZbqbVA'
	secret = 'JU1gQk99VpAEZWWKxiR97w8mIPtSZsXwuORL6H2NKkve0EHDvBZ5IQN-CXHqMhVKmOLRcRhjyr4RPnTqAmD5Ig'
	cloudstack = CloudStack.Client(api, apikey, secret) # ouvrir une connexion serveur/client	
	
	cloudstack.createTemplate({
	'displaytext':displaytext ,
	'name':name,
	'ostypeid':ostypeid,
	'bits':'64',
	'isfeatured':'true',
	'ispublic':'true',
	'volumeid':volumeid
	})


def startVM(request,id):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()	
	api = 'http://196.203.216.18:5555/client/api'
	apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
	secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'
	cloudstack = CloudStack.Client(api, apikey, secret) # ouvrir une connexion serveur/client
	c.execute("SELECT vmid FROM vmm_vm where id ="+id+";");
	vmid, = c.fetchone()
        vm = cloudstack.startVirtualMachine({'id':vmid})

	virtualMachine = set(vm)

	c.execute("UPDATE vmm_vm SET state='Running' WHERE Id='"+id+"';")
	
	now = datetime.datetime.now()
	now=str(now)
	
	#c.execute("INSERT INTO log_event (id,username,role,description,date,type,vmname) VALUES (NULL,'"+
	#request.session["username"]+"','"+request.session["role"]+"','started the machine :','"+now+"','VM.START','"++"');")

	conn.commit()
	conn.close()	
	return render_to_response('vm.html',{'vm':Vm.objects.get(id=id),'role':request.session["role"],'username':request.session["username"]})

def restartVM(request,id):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()	
	api = 'http://196.203.216.18:5555/client/api'
	apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
	secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'
	cloudstack = CloudStack.Client(api, apikey, secret) # ouvrir une connexion serveur/client
	c.execute("SELECT vmid FROM vmm_vm where id ="+id+";");
	conn.commit()
	vmid, = c.fetchone()	
	vm = cloudstack.rebootVirtualMachine({'id':vmid})
	conn.close()
	return render_to_response('vm.html',{'vm':Vm.objects.get(id=id),'role':request.session["role"],'username':request.session["username"]})


def stopVM(request,id):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()	
	api = 'http://196.203.216.18:5555/client/api'
	apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
	secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'
	cloudstack = CloudStack.Client(api, apikey, secret) # ouvrir une connexion serveur/client
	c.execute("SELECT vmid FROM vmm_vm where id ="+id+";");
	conn.commit()
	vmid, = c.fetchone()	
        vm = cloudstack.stopVirtualMachine({'id':vmid})
	c.execute("UPDATE vmm_vm SET state='Stopped' WHERE Id='"+id+"';")
	conn.commit()
	conn.close()	
	return render_to_response('vm.html',{'vm':Vm.objects.get(id=id),'role':request.session["role"],'username':request.session["username"]})


def destroyVM(request,id):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()	
	api = 'http://196.203.216.18:5555/client/api'
	apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
	secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'
	cloudstack = CloudStack.Client(api, apikey, secret) # ouvrir une connexion serveur/client
	c.execute("SELECT vmid FROM vmm_vm where id ="+id+";");
	conn.commit()
	vmid = c.fetchone()[0]
	vm = cloudstack.destroyVirtualMachine({'id':vmid})
	c.execute("DELETE FROM vmm_vm WHERE id = '"+id+"';")
	conn.commit()
	conn.close()
	return  HttpResponseRedirect("/allVms")

def listAllVMs(request):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()
	api = 'http://196.203.216.18:5555/client/api'
	apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
	secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'
	cloudstack = CloudStack.Client(api, apikey, secret) # ouvrir une connexion serveur/client	
	c.execute("DELETE FROM vmm_vm ;")
	conn.commit()
	vms = cloudstack.listVirtualMachines()
	
	for vm in vms:
		if vm['templateid'] == "22cff7e4-af82-408f-a400-221b5fb4ae2a":
			c.execute("INSERT INTO vmm_vm (name,vmid,serviceoffering,templateid,zoneid,networkids,volumeid,state,image) VALUES ('"
			+vm['displayname']+ "','"+vm['id']+"','98d17394-e6cf-4f9d-b84f-82b3855ea78b','"
			+vm['templateid']+"','95cddc7f-bc1b-4014-a7b4-585dcd684e01','87e115e8-3849-4961-824c-0c8cb8e86c76','0','"+vm['state']+"','assets/images/centos.png')")
			conn.commit()
		elif vm['templateid'] == "26dcfbfe-bad9-4bce-924d-9898bb54a5c8":
			c.execute("INSERT INTO vmm_vm (name,vmid,serviceoffering,templateid,zoneid,networkids,volumeid,state,image) VALUES ('"
			+vm['displayname']+ "','"+vm['id']+"','98d17394-e6cf-4f9d-b84f-82b3855ea78b','"
			+vm['templateid']+"','95cddc7f-bc1b-4014-a7b4-585dcd684e01','87e115e8-3849-4961-824c-0c8cb8e86c76','0','"+vm['state']+"','assets/images/ubuntu.png')")
			conn.commit()
		elif vm['templateid'] == "62a3d073-c843-48fb-a06a-94c5ae6c9987":
			c.execute("INSERT INTO vmm_vm (name,vmid,serviceoffering,templateid,zoneid,networkids,volumeid,state,image) VALUES ('"
			+vm['displayname']+ "','"+vm['id']+"','98d17394-e6cf-4f9d-b84f-82b3855ea78b','"
			+vm['templateid']+"','95cddc7f-bc1b-4014-a7b4-585dcd684e01','87e115e8-3849-4961-824c-0c8cb8e86c76','0','"+vm['state']+"','assets/images/debian.jpg')")
			conn.commit()
	
	return render_to_response('vms.html',{'vms':Vm.objects.all(),'role':request.session["role"],'username':request.session["username"]})


#def listAllFirewallRules():
  #  api = 'http://196.203.216.18:5555/client/api'
	#apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
	#secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'
	#cloudstack = CloudStack.Client(api, apikey, secret)
	#rules  = cloudstack.listFirewallRules()
	#for rule in rules:
		#print "rule made on port : %s"% (rule['endport'])
	#return render_to_response('Fws.html',{'rules':Fw.objects.all()})

def restoreVM(VMid):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()	
	api = 'http://196.203.216.18:5555/client/api'
	apikey = '3U7UPLR4JHYEzOhKe0JYnR_ICChdmuynnl0SdqmFzFgG4Hgd6BJHHjcSk2K3SsXUvheLEoN-SlRuEOpqZbqbVA'
	secret = 'JU1gQk99VpAEZWWKxiR97w8mIPtSZsXwuORL6H2NKkve0EHDvBZ5IQN-CXHqMhVKmOLRcRhjyr4RPnTqAmD5Ig'
	cloudstack = CloudStack.Client(api, apikey, secret) # ouvrir une connexion serveur/client
	c.execute("SELECT vmid FROM vmm_vm where id ="+id+";");
	conn.commit()
	vmid = c.fetchone()[0]
        vm = cloudstack.restoreVirtualMachine({'id':VMid})
	conn.close()
	return render_to_response('vm.html',{'vm':Vm.objects.get(id=id),'role':request.session["role"],'username':request.session["username"]})

def createVM(request):
	conn = sqlite3.connect('testDB')
	c = conn.cursor()
	api = 'http://196.203.216.18:5555/client/api'
	apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
	secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'
	cloudstack = CloudStack.Client(api, apikey, secret) # ouvrir une connexion serveur/client
	
	vm = cloudstack.deployVirtualMachine(
	{
	'serviceofferingid':'98d17394-e6cf-4f9d-b84f-82b3855ea78b',
	'templateid':request.POST['templateid'],
	'zoneid':'95cddc7f-bc1b-4014-a7b4-585dcd684e01',
	'networkids': 'a4736f46-c8c8-494c-9a84-aaabaf3055d9',
	'displayname':request.POST['name'],
	})
	if request.POST['templateid'] == "22cff7e4-af82-408f-a400-221b5fb4ae2a":
		c.execute("INSERT INTO vmm_vm (name,vmid,serviceoffering,templateid,zoneid,networkids,volumeid,image) VALUES ('"
		+request.POST['name']+ "','"+vm['id']+"','98d17394-e6cf-4f9d-b84f-82b3855ea78b','"
		+request.POST['templateid']+"','95cddc7f-bc1b-4014-a7b4-585dcd684e01','87e115e8-3849-4961-824c-0c8cb8e86c76','0','assets/images/centos.png');")
	if request.POST['templateid'] == "26dcfbfe-bad9-4bce-924d-9898bb54a5c8":
		c.execute("INSERT INTO vmm_vm (name,vmid,serviceoffering,templateid,zoneid,networkids,volumeid,image) VALUES ('"
		+request.POST['name']+ "','"+vm['id']+"','98d17394-e6cf-4f9d-b84f-82b3855ea78b','"
		+request.POST['templateid']+"','95cddc7f-bc1b-4014-a7b4-585dcd684e01','87e115e8-3849-4961-824c-0c8cb8e86c76','0','assets/images/ubuntu.png');")
	if request.POST['templateid'] == "62a3d073-c843-48fb-a06a-94c5ae6c9987":
		c.execute("INSERT INTO vmm_vm (name,vmid,serviceoffering,templateid,zoneid,networkids,volumeid,image) VALUES ('"
		+request.POST['name']+ "','"+vm['id']+"','98d17394-e6cf-4f9d-b84f-82b3855ea78b','"
		+request.POST['templateid']+"','95cddc7f-bc1b-4014-a7b4-585dcd684e01','87e115e8-3849-4961-824c-0c8cb8e86c76','0','assets/images/debian.jpg');")
	
	conn.commit()

	conn.close()
	return render_to_response('vms.html',{'vms':Vm.objects.all(),'role':request.session["role"],'username':request.session["username"]})







