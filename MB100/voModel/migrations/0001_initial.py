# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoComData',
            fields=[
                ('dataId', models.IPAddressField(serialize=False, primary_key=True)),
                ('dataName', models.CharField(max_length=50)),
                ('dataDescription', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoComUser',
            fields=[
                ('userId', models.IPAddressField(serialize=False, primary_key=True)),
                ('userName', models.CharField(max_length=50)),
                ('userPwd', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoDbinfCategory',
            fields=[
                ('cateId', models.IPAddressField(serialize=False, primary_key=True)),
                ('cdcName', models.CharField(max_length=50)),
                ('intro', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoDbinfInfo',
            fields=[
                ('infoId', models.IPAddressField(serialize=False, primary_key=True)),
                ('createorId', models.CharField(max_length=50)),
                ('stat', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('keyword', models.CharField(max_length=50)),
                ('cdfContent', models.CharField(max_length=50)),
                ('createDate', models.CharField(max_length=50)),
                ('coId', models.ForeignKey(related_name='coId', to='voModel.CoDbinfCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoIntegral',
            fields=[
                ('id', models.IPAddressField(serialize=False, primary_key=True)),
                ('score', models.FloatField(max_length=30)),
                ('deptName', models.CharField(max_length=50)),
                ('sort', models.IntegerField()),
                ('ptnrId', models.ForeignKey(related_name='ptnrIdHZ', to='voModel.CoComUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoInvtInf',
            fields=[
                ('invtId', models.IPAddressField(serialize=False, primary_key=True)),
                ('rcSubject', models.CharField(max_length=50)),
                ('resSort', models.CharField(max_length=50)),
                ('startTime', models.CharField(max_length=50)),
                ('rcTime', models.CharField(max_length=50)),
                ('mnTudget', models.CharField(max_length=50)),
                ('rcNum', models.CharField(max_length=50)),
                ('rcIntro', models.CharField(max_length=50)),
                ('faceWay', models.CharField(max_length=50)),
                ('rcCriterion', models.CharField(max_length=50)),
                ('advertObject', models.CharField(max_length=50)),
                ('rcType', models.CharField(max_length=50)),
                ('units', models.CharField(max_length=50)),
                ('creatorId', models.CharField(max_length=50)),
                ('endFlag', models.CharField(max_length=50)),
                ('opStatus', models.CharField(max_length=50)),
                ('endDate', models.CharField(max_length=50)),
                ('runUnit', models.CharField(max_length=50)),
                ('result', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoInvtResponse',
            fields=[
                ('respId', models.IPAddressField(serialize=False, primary_key=True)),
                ('runUnit', models.CharField(max_length=50)),
                ('linkman', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('responseStatus', models.CharField(max_length=50)),
                ('rcStatus', models.CharField(max_length=50)),
                ('schemaDesc', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=50)),
                ('submitDate', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=50)),
                ('attachment', models.CharField(max_length=50)),
                ('opFlag', models.CharField(max_length=50)),
                ('rcSubject', models.CharField(max_length=50)),
                ('deptName', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoPtnrInf',
            fields=[
                ('spId', models.IPAddressField(serialize=False, primary_key=True)),
                ('deptName', models.CharField(max_length=50)),
                ('deptType', models.CharField(max_length=50)),
                ('resType', models.CharField(max_length=50)),
                ('mgtMode', models.CharField(max_length=50)),
                ('crtDate', models.CharField(max_length=50)),
                ('peopNum', models.CharField(max_length=50)),
                ('brandName', models.CharField(max_length=50)),
                ('mngType', models.CharField(max_length=50)),
                ('manMkt', models.CharField(max_length=50)),
                ('deptAddr', models.CharField(max_length=50)),
                ('artPerson', models.CharField(max_length=50)),
                ('principalName', models.CharField(max_length=50)),
                ('principalTel', models.CharField(max_length=50)),
                ('principalMtel', models.CharField(max_length=50)),
                ('businessNo', models.CharField(max_length=50)),
                ('regAddr', models.CharField(max_length=50)),
                ('taxRegNo', models.CharField(max_length=50)),
                ('deptBrief', models.CharField(max_length=50)),
                ('coLevel', models.CharField(max_length=50)),
                ('creditLevel', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('opStatus', models.CharField(max_length=50)),
                ('regDate', models.CharField(max_length=50)),
                ('tian', models.IntegerField()),
                ('sisi', models.IntegerField()),
                ('username', models.CharField(max_length=50)),
                ('userpwd', models.CharField(max_length=50)),
                ('score', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('userId', models.ForeignKey(related_name='userIdHZ', to='voModel.CoComUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoSlctList',
            fields=[
                ('slctId', models.IPAddressField(serialize=False, primary_key=True)),
                ('subject', models.CharField(max_length=50)),
                ('createUserId', models.CharField(max_length=50)),
                ('createDate', models.DateTimeField(max_length=50)),
                ('belongYear', models.CharField(max_length=50)),
                ('belongMonth', models.CharField(max_length=50)),
                ('opFlag', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoSlctSchema',
            fields=[
                ('schemaId', models.IPAddressField(serialize=False, primary_key=True)),
                ('schemaName', models.CharField(max_length=50)),
                ('schemaDesc', models.CharField(max_length=300)),
                ('createDate', models.DateTimeField()),
                ('summing', models.CharField(max_length=50)),
                ('dealStatus', models.CharField(max_length=50)),
                ('slctType', models.CharField(max_length=50)),
                ('attachment', models.FileField(max_length=50, upload_to=b'')),
                ('opStatus', models.FileField(max_length=10, upload_to=b'')),
                ('ptnrId', models.ForeignKey(related_name='ptnrIdCS', to='voModel.CoPtnrInf')),
                ('slctListId', models.ForeignKey(related_name='slctListId', to='voModel.CoSlctList')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoWformFdbk',
            fields=[
                ('wfkId', models.IPAddressField(serialize=False, primary_key=True)),
                ('cyfContent', models.CharField(max_length=50)),
                ('replyId', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CoWformInf',
            fields=[
                ('wfId', models.IPAddressField(serialize=False, primary_key=True)),
                ('cwiName', models.CharField(max_length=50)),
                ('cwiType', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=50)),
                ('timeLimt', models.CharField(max_length=50)),
                ('sendTo', models.CharField(max_length=50)),
                ('createDate', models.CharField(max_length=50)),
                ('cwiContent', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('statu', models.CharField(max_length=50)),
                ('createUserId', models.ForeignKey(related_name='createUserId', to='voModel.CoComUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SysAdmin',
            fields=[
                ('adminId', models.IPAddressField(serialize=False, primary_key=True)),
                ('adminName', models.CharField(max_length=50)),
                ('adminPwd', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cowformfdbk',
            name='wformId',
            field=models.ForeignKey(related_name='wformId', to='voModel.CoWformInf'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coinvtresponse',
            name='ptnrId',
            field=models.ForeignKey(related_name='ptnrIdCI', to='voModel.CoPtnrInf'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coinvtresponse',
            name='rcId',
            field=models.ForeignKey(related_name='rcId', to='voModel.CoInvtInf'),
            preserve_default=True,
        ),
    ]
