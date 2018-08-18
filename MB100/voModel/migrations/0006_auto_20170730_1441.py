# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voModel', '0005_auto_20170730_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowformfdbk',
            name='replyId',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
