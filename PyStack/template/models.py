from django.db import models


class Template(models.Model):

    displaytext = models.CharField(
        max_length=255,
    )

    name = models.CharField(
        max_length=255,

    )

    ostypeid = models.CharField(
        max_length=255,

    )
    bits = models.CharField(
        max_length=255,

    )
    isfeatured = models.CharField(
        max_length=255,

    )
    
    ispublic = models.CharField(
        max_length=255,

    )
    
    volumeid = models.CharField(
        max_length=255,

    )

    
