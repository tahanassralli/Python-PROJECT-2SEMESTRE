# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pw', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipaddressid', models.CharField(max_length=255)),
                ('privateport', models.CharField(max_length=255)),
                ('protocol', models.CharField(max_length=255)),
                ('publicport', models.CharField(max_length=255)),
                ('virtualmachineid', models.CharField(max_length=255)),
                ('networkids', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Pw',
        ),
    ]
