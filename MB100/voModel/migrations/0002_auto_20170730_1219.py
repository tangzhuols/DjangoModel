# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysadmin',
            name='adminId',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
