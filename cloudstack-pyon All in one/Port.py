#!/usr/bin/python

import CloudStack

api = 'http://196.203.216.18:5555/client/api'
apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)


cloudstack.createPortForwardingRule({
    'ipaddressid':'eb03d24a-d005-4828-b740-20a1b4ce38ba',
    'privateport':'53',
    'protocol':'TCP',
    'publicport':'5555',
    'virtualmachineid':'6f1eb0c3-28c1-4555-b388-963e67a108ab',
    #'cidrlist':'172.16.2.2/16',
    #'openfirewall': 'true',
    #'networkid':'a4736f46-c8c8-494c-9a84-aaabaf3055d9'
    }
    )
