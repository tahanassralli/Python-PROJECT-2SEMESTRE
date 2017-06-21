#!/usr/bin/python

import CloudStack
api = 'http://196.203.216.18:5555/client/api'
#api = 'http://172.16.206.31:8080/client/api'

apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)

id='6f1eb0c3-28c1-4555-b388-963e67a108ab'
request = {
        'id': id,
    }


print "\n################# VM Menu  ###################"
print "\nEnter Command"
while 1:
    print "'1'to Start VM"
    print "'0'to Stop  VM"
    print "'R'to Reboot  VM"
    print "'D'to Destroy VM"

    
    x=raw_input()
    if   x== "1":
        startVm = cloudstack.startVirtualMachine(request)
        print "VM being Starting. vm id = %s" % id
        ##break
    elif x== "0":
        StopVm = cloudstack.stopVirtualMachine(request)
        print "VM being Stoping. vm id = %s" % id
        ##break 
    elif x== "R":
        RebootVm = cloudstack.rebootVirtualMachine(request)
        print "VM being Rebooting. vm id = %s" % id
        ##break
    elif x== "D": 
        DestroyVm = cloudstack.destroyVirtualMachine(request)
        print "VM being Destoyed. vm id = %s" % id
        ##  break
    











