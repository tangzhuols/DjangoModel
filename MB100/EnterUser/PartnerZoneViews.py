# coding:utf-8
# 合作伙伴专区
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

# 首页代码
def CodeHomeControl(request):
    return render(request, 'form/code.html')