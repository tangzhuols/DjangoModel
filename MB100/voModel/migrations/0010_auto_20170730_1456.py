# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voModel', '0009_auto_20170730_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coslctschema',
            name='schemaName',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
