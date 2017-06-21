"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from vmm.models import Vm

from django.test import TestCase
from backend import CloudStack

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        api = 'http://172.18.1.64:8080/client/api'
        apikey = 'l46VQh0GlygXrtqezbP-LjSpe-8r4Tu0KhykldnU16PJdG9PjWRvJJkRC8lwbINpJG1DfTV6PymFf-9f65XVXQ'
        secret = '1_9_aGMA1XWK4wUuvVyLgD6UGCk-qjD2FqP_gDSsdiDzT-rGxaTI_TMdoHP73TxTAZGTCK28eMNmmCAUYG--7Q'

        cloudstack = CloudStack.Client(api, apikey, secret)



        job = cloudstack.deployVirtualMachine({
        'displayname':'testVM',
        'serviceofferingid': '98d17394-e6cf-4f9d-b84f-82b3855ea78b',
        'templateid': '22cff7e4-af82-408f-a400-221b5fb4ae2a',
        'zoneid': '95cddc7f-bc1b-4014-a7b4-585dcd684e01',
        'networkids':'d17f655f-ddbe-4be2-ba91-e474678aee87',
        })
        print "VM being deployed. Job id = %s" % job['jobid']
        newvm = Vm(name = 'testVM',vmid = job['id'],serviceoffering='98d17394-e6cf-4f9d-b84f-82b3855ea78b', templateid= '22cff7e4-af82-408f-a400-221b5fb4ae2a',zoneid ='95cddc7f-bc1b-4014-a7b4-585dcd684e01',networkids='d17f655f-ddbe-4be2-ba91-e474678aee87')
        
        self.assertEquals(
            str(newvm),
            'testVM',
        )


