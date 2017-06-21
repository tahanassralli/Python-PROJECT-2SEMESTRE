from django.db import models

class Vm(models.Model):

    name = models.CharField(
        max_length=255,
    )
    vmid = models.CharField(
        max_length=255,

    )
    serviceoffering = models.CharField(
        max_length=255,

    )
    templateid = models.CharField(
        max_length=255,

    )
    zoneid = models.CharField(
        max_length=255,

    )
    
    networkids = models.CharField(
        max_length=255,

    )
    
    volumeid = models.CharField(
        max_length=255,

    )

    state = models.CharField(
        max_length=255,

    )

    image = models.CharField(
        max_length=255,

    )
 
    def __str__(self):

        return ' '.join([
            self.name,
            self.vmid,
            
        ])
		
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
