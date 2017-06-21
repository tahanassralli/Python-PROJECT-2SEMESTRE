#!/usr/bin/python

import CloudStack


api = 'http://196.203.216.18:5555/client/api'
#api = 'http://172.16.206.31:8080/client/api'
apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)


##
##vms= cloudstack.listEventTypes()
##for vm in vms:
##            print "\n %s" % (vm['name'] )
##           

events= cloudstack.listEvents({
        'startdate': '2015-04-20',
        })

print"\n*****************Events From *************"
print "\naccount  created  Domain  Description"
for event in events:
    print "\n%s %s %s %s %s %s %s" % ( event['account'],event['created'],event['domain'],event['type'],event['description'],event['level'],event['state'])
    ##print " IDVM : %s\n Name: %s\n State: %s\n Zone: %s\n Creation Date : %s\n IP Address: %s\n High Availability: %s\n Template Name: %s\ CPUs: %s\n CPU Frequency: %s Mhz\n Memory: %s\n"%(vm['id'], vm['name'], vm['state'], vm['zoneid'], vm['created'],vm['nic'][0]['ipaddress'],vm['haenable'],vm['templatename'],vm['cpunumber'],vm['cpuspeed'],vm['memory'])
    ##break

##request = {
##        'displaytext': 'CentOSServerbaseif',
##        'name':'TempCentOS',
##        'ostypeid':'a01b94c6-a166-11e4-b2ef-005056847688',
##        #'virtualmachineid':'6f1eb0c3-28c1-4555-b388-963e67a108ab',
##        'volumeid':'37e7bce9-94df-4bfc-9369-8447530c9dd3',
##        #'snapshotid':'
##    }

##cloudstack.createTemplate({
##    'displaytext':'TemBASeif',
##    'name':'TempBqSeif',
##    'ostypeid':'a01b94c6-a166-11e4-b2ef-005056847688',
##    'bits':'64',
##    'isfeatured':'true',
##    'ispublic':'true',
##    'volumeid':'37e7bce9-94df-4bfc-9369-8447530c9dd3'
##    }
                         # )

##cloudstack.createTemplate(request)
##print cloudstack.listTemplates({
##        'templatefilter':'executable'
##
##    })



