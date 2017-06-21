import CloudStack
from vmm.models import Fw
from pw.models import Vm

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

api = 'http://196.203.216.18:5555/client/api'


apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)


def deployvm(request):
    
    job = cloudstack.createFirewallRule({
    'cidrlist':request.POST['cidrlist'],
    'startport': request.POST['startport'],
    'ipaddressid': request.POST['ipaddressid'],
    'endport': request.POST['endport'],
    'protocol':request.POST['protocol'],
    })
    print "VM being deployed. Job id = %s" % job['jobid']
    Fw.objects.create(cidrlist = request.POST['cidrlist'],startport = request.POST['startport'],endport=request.POST['endport'], ipaddressid= request.POST['ipaddressid'])
    
    
    return render_to_response('vms.html',{'vms':Vm.objects.all(),'role':request.session["role"],'username':request.session["username"]})

#deployvm("adminvm")
def deploypw(request):
    
    job = cloudstack.createPortForwardingRule({
    'ipaddressid':request.POST['ipaddressid'],
    'privateport': request.POST['privateport'],
    'protocol': request.POST['protocol'],
    'publicport': request.POST['publicport'],
    'virtualmachineid':request.POST['virtualmachineid'],
    })
    print "VM being deployed. Job id = %s" % job['jobid']
   # Vm.objects.create(ipaddressid = request.POST['ipaddressid'],privateport = request.POST['privateport'],protocol=request.POST['protocol'], publicport= request.POST['publicport'],virtualmachineid= request.POST['virtualmachineid'],networkids= request.POST['networkids'])
    
    
    return render_to_response('vms.html',{'vms':Vm.objects.all(),'role':request.session["role"],'username':request.session["username"]})




