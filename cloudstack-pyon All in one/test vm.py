#!/usr/bin/python

import CloudStack

api = 'http://172.16.206.31:8080/client/api'
apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'
cloudstack = CloudStack.Client(api, apikey, secret)
id='7dd0f66b-3ae7-47c1-bcfb-9ef3a8e0678e'
request = {
        'id': id,
    }

cloudstack.stopVirtualMachine(request)

  











