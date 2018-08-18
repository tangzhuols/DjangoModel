# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voModel', '0008_auto_20170730_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoWformFdbk',
            fields=[
                ('wfkId', models.AutoField(serialize=False, primary_key=True)),
                ('cyfContent', models.CharField(max_length=50, null=True)),
                ('replyId', models.CharField(max_length=50)),
                ('wformId', models.ForeignKey(related_name='wformId', to='voModel.CoWformInf')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cowformfdb',
            name='replyId',
        ),
        migrations.RemoveField(
            model_name='cowformfdb',
            name='wformId',
        ),
        migrations.DeleteModel(
            name='CoWformFdb',
        ),
    ]
