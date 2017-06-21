from django.db import models
from backend import CloudStack

api = 'http://172.18.1.64:8080/client/api'
apikey = 'l46VQh0GlygXrtqezbP-LjSpe-8r4Tu0KhykldnU16PJdG9PjWRvJJkRC8lwbINpJG1DfTV6PymFf-9f65XVXQ'
secret = '1_9_aGMA1XWK4wUuvVyLgD6UGCk-qjD2FqP_gDSsdiDzT-rGxaTI_TMdoHP73TxTAZGTCK28eMNmmCAUYG--7Q'

cloudstack = CloudStack.Client(api, apikey, secret)
# Create your models here.
class Vm(models.Model):

    ipaddressid = models.CharField(
        max_length=255,
    )
    privateport = models.CharField(
        max_length=255,

    )
    protocol = models.CharField(
        max_length=255,

    )
    publicport = models.CharField(
        max_length=255,

    )
    virtualmachineid = models.CharField(
        max_length=255,

    )
    
    networkids = models.CharField(
        max_length=255,

    )
    
   
    """
    def __init__(self):

        job = cloudstack.deployVirtualMachine({
        'displayname':self.name,
        'serviceofferingid': '98d17394-e6cf-4f9d-b84f-82b3855ea78b',
        'templateid': '22cff7e4-af82-408f-a400-221b5fb4ae2a',
        'zoneid': '95cddc7f-bc1b-4014-a7b4-585dcd684e01',
        'networkids':'d17f655f-ddbe-4be2-ba91-e474678aee87',
        })
        print "VM being deployed. Job id = %s" % job['jobid']
        #Vm.objects.create(name = name,vmid = job['id'],serviceoffering='98d17394-e6cf-4f9d-b84f-82b3855ea78b', templateid= '22cff7e4-af82-408f-a400-221b5fb4ae2a',zoneid ='95cddc7f-bc1b-4014-a7b4-585dcd684e01',networkids='d17f655f-ddbe-4be2-ba91-e474678aee87')
        
        return
    """   
        
        
        
        
        
    def __str__(self):

        return ' '.join([
            self.virtualmachineid,
            self.ipaddressid,
            
        ])