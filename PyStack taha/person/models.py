from django.db import models

class Person(models.Model):

    username = models.CharField(
        max_length=255,
    )
    password = models.CharField(
        max_length=255,

    )
    role = models.CharField(
        max_length=255,

    )
    sexe = models.CharField(
        max_length=255,

    )
    
