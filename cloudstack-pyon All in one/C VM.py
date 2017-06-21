#!/usr/bin/python

import CloudStack


api = 'http://196.203.216.18:5555/client/api'
#api = 'http://172.16.206.31:8080/client/api'
apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)

job = cloudstack.deployVirtualMachine({
   #0# 'serviceofferingid': '83c21deb-8a08-4add-b1b6-8c30eb45fed2',
    'serviceofferingid': '98d17394-e6cf-4f9d-b84f-82b3855ea78b',
    'templateid':        '22cff7e4-af82-408f-a400-221b5fb4ae2a',
    'zoneid':            '95cddc7f-bc1b-4014-a7b4-585dcd684e01',
    'name' : 'Jassserveruub',
    'networkids': 'a4736f46-c8c8-494c-9a84-aaabaf3055d9',
})

print "VM being deployed. Job id = %s" % job['jobid']

print "All Jobs:"
jobs = cloudstack.listAsyncJobs({})
for job in jobs:
   print  "%s : %s, status = %s" % (job['jobid'], job['cmd'], job['jobstatus'])
    
