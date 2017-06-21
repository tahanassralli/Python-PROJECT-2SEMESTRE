
import CloudStack

api = 'http://196.203.216.18:5555/client/api'
apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)


cloudstack.createFirewallRule({
    'cidrlist':'0.0.0.0/0',
    'startport':'7777',
    'endport':'7777',
    'ipaddressid':'eb03d24a-d005-4828-b740-20a1b4ce38ba',
    'protocol':'TCP',
    #'cidrlist':'172.16.2.2/16',
    #'openfirewall': 'true',
    #'networkid':'a4736f46-c8c8-494c-9a84-aaabaf3055d9'
    }
    )
