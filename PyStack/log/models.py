from django.db import models

# Create your models here.

class Event(models.Model):

    username = models.CharField(
        max_length=255,
    )
    role = models.CharField(
        max_length=255,

    )
    description = models.CharField(
        max_length=255,

    )
    date = models.CharField(
        max_length=255,

    )
    type = models.CharField(
        max_length=255,

    )
