#!/usr/bin/python

import CloudStack

api = 'http://172.16.206.31:8080/client/api'
apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)


cloudstack.createPortForwardingRule({
    'ipaddressid':'a4736f46-c8c8-494c-9a84-aaabaf3055d9',
    'privateport':'22',
    'protocol':'TCP',
    'publicport':'4444',
    'virtualmachineid':'c1d28008-ba24-43bd-be53-8d1aed7c7f6f'
    #'cidrlist':'172.16.2.2/16',
    #'openfirewall': 'true',
    #'networkid':'a4736f46-c8c8-494c-9a84-aaabaf3055d9'
    }
    )
