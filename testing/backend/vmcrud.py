import CloudStack
from vmm.models import Vm
from django.http import HttpResponse

api = 'http://172.18.1.64:8080/client/api'
apikey = 'l46VQh0GlygXrtqezbP-LjSpe-8r4Tu0KhykldnU16PJdG9PjWRvJJkRC8lwbINpJG1DfTV6PymFf-9f65XVXQ'
secret = '1_9_aGMA1XWK4wUuvVyLgD6UGCk-qjD2FqP_gDSsdiDzT-rGxaTI_TMdoHP73TxTAZGTCK28eMNmmCAUYG--7Q'

cloudstack = CloudStack.Client(api, apikey, secret)


def deployvm(request):
    
    job = cloudstack.deployVirtualMachine({
    'displayname':request.POST['name'],
    'serviceofferingid': request.POST['serviceoffering'],
    'templateid': request.POST['templateid'],
    'zoneid': request.POST['zoneid'],
    'networkids':request.POST['networkids'],
    })
    print "VM being deployed. Job id = %s" % job['jobid']
    Vm.objects.create(name = request.POST['name'],vmid = job['id'],serviceoffering=request.POST['serviceoffering'], templateid= request.POST['templateid'],zoneid =request.POST['zoneid'],networkids=request.POST['networkids'])
    
    print request.POST['networkids']
    return HttpResponse("Created")

#deployvm("adminvm")


