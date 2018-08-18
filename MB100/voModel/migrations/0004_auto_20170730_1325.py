# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voModel', '0003_auto_20170730_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sysadmin',
            name='adminName',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sysadmin',
            name='adminPwd',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
