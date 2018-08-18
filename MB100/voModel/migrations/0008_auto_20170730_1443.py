# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voModel', '0007_auto_20170730_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoWformFdb',
            fields=[
                ('wfkId', models.AutoField(serialize=False, primary_key=True)),
                ('cyfContent', models.CharField(max_length=50, null=True)),
                ('replyId', models.ForeignKey(to='voModel.CoComUser')),
                ('wformId', models.ForeignKey(related_name='wformId', to='voModel.CoWformInf')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cowformfdbk',
            name='replyId',
        ),
        migrations.RemoveField(
            model_name='cowformfdbk',
            name='wformId',
        ),
        migrations.DeleteModel(
            name='CoWformFdbk',
        ),
    ]
