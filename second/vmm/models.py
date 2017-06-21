from django.db import models
from backend import CloudStack

api = 'http://196.203.216.18:5555/client/api'
##api = 'http://172.16.206.31:8080/client/api'

apikey = 'P_QzAVnZVDPzj38X8XI2U-BLqzzsmxJSB7rwYD4i2nSsK72aFsTuEoaCTXxCOf-C3VmAOdgkdpRWKQRqgPSFZA'
secret = 'RzAk3h3dOHwwdj6GD_v5n8OIjFNoxSLEIwIQDuznrZeGW0v5uaHe2fmdQ2K43cXCOmEk0uk80Ut8Ui7lk22tZA'

cloudstack = CloudStack.Client(api, apikey, secret)
# Create your models here.
class Fw(models.Model):

    cidrlist = models.CharField(
        max_length=255,
    )
    startport = models.CharField(
        max_length=255,

    )
    endport = models.CharField(
        max_length=255,

    )
    ipaddressid = models.CharField(
        max_length=255,

    )
	
   
 
def __str__(self):

        return ' '.join([
            self.cidrlist,
            self.startport,
            
        ])