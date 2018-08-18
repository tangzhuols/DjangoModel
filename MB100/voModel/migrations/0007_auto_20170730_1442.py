# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voModel', '0006_auto_20170730_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowformfdbk',
            name='replyId',
            field=models.ForeignKey(to='voModel.CoComUser'),
            preserve_default=True,
        ),
    ]
