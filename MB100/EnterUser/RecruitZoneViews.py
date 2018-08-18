# coding:utf-8
# 招募专区
from django.shortcuts import render

from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext
from form import LoginForm
from voModel.models import CoComUser
from django.http import HttpResponse
from voModel import models
from django.db import connection, transaction
import json


# 招募详情
def RecruitmentOne(request):
    if request.method == 'GET':
        invtId = request.GET.get('invtId')
        CoInvtInf = models.CoInvtInf.objects.get(invtId=invtId)
        cursor = connection.cursor()
        sql = "SELECT * FROM vomodel_CoInvtResponse WHERE rcId_id = %s"
        cursor.execute(sql, [CoInvtInf.invtId])
        CoInvtResponse = cursor.fetchall()
        cursor.close()
        CoInvtRespons = []
        for item in CoInvtResponse:
            CoNe = {}
            CoNe['id'] = item[1]
            CoNe['name'] = item[2]
            CoNe['day'] = item[5]
            if item[13] == '1':
                CoNe['address'] = "未中标"
            else:
                CoNe['address'] = "中标"
            CoInvtRespons.append(CoNe)
    return render_to_response('detail/example.html', {'CoInvtInf': CoInvtInf, 'CoInvtResponse': json.dumps(CoInvtRespons)})
