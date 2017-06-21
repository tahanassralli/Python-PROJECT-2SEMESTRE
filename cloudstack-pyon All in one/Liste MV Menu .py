##!/usr/bin/python

import CloudStack

api = 'http://196.203.216.18:5555/client//api'
##api = 'http://172.16.206.31:8080/client/api'
apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)

networkid='a4736f46-c8c8-494c-9a84-aaabaf3055d9'
requestNet = {
        'networkid': networkid,
    }

domainid='Root'
requestDom = {
        'domainid': domainid,
    }



print "\n################# Liste MV Menu  ###################"

while 1:
    print "\n Enter Command"
    print "'A'to List all Virtual Machines"
    print "'N'to List Virtual Machines by Network"
    print "'D'to List Virtual Machines* by Domain"
    print "'I'to List all Instances"
    
    x=raw_input()
    if   x== "A":
         vms = cloudstack.listVirtualMachines()
         print"\n*****************List Of Virtual Machines*************"
         for vm in vms:
            #print "\n %s \n %s \n %s" % (vm['id'], vm['name'], vm['state'])
            print " IDVM : %s\n Name: %s\n State: %s\n Zone: %s\n Creation Date : %s\n IP Address: %s\n High Availability: %s\n Template Name: %s\ CPUs: %s\n CPU Frequency: %s Mhz\n Memory: %s\n"%(vm['id'], vm['name'], vm['state'], vm['zoneid'], vm['created'],vm['nic'][0]['ipaddress'],vm['haenable'],vm['templatename'],vm['cpunumber'],vm['cpuspeed'],vm['memory'])
            print"\n******************************************************"
        ##break
    elif x== "N":
        vmsbynet=cloudstack.listVirtualMachines(requestNet)
        print"\n**********List Of Virtual Machines* by Network*******"
        for vmbynet in vmsbynet:
            print "\n id=%s \n name=%s \n Sate=%s" % (vmbynet['id'], vmbynet['name'], vmbynet['state']  )
            print"\n******************************************************"
       ## break
    elif x== "D":
        vmsbydom=cloudstack.listVirtualMachines(requestDom)
        print"\n**********List Of Virtual Machines by Domain*******"
        for vmbydom in vmsbydom:
            print "\n id=%s \n name=%s \n Sate=%s" % (vmbydom['id'], vmbydom['name'], vmbydom['state']  )
            print"\n******************************************************"
       ## break
    elif x== "I":
        insts= cloudstack.listInstanceGroups()
        print"\n*****************List Of Instances ********************"
        for inst in insts:
            print "\n%s \nn%s \n%s" % (inst['id'], inst['name'],inst['domain'])
            print"\n******************************************************"
        ##break


