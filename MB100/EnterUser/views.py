# coding:utf-8
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
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import time, datetime


# Create your views here.
# 程序页面入口
def index(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.jsp', RequestContext(request, {'form': form}))
        # return render(request, 'login.html')
    else:
        form = LoginForm(request.Post)
        if form.is_valid():
            userName = request.Post.get('userName', '')
            userPwd = request.Post.get('userPwd', '')
            print (userName)


# 前台用户认证登录
@csrf_exempt
def enterUsers(request):
    # for lists in coComUser:
    form = LoginForm(request.POST)
    if form.is_valid():
        userName = '%s' % request.POST.get('userName')
        userPwd = '%s' % request.POST.get('userPwd')
        sql = "SELECT * FROM vomodel_cocomuser u join vomodel_coptnrinf cp on u.userId = cp.userId_id WHERE u.userName='%s' AND u.userPwd='%s'" % (
            userName, userPwd)
        cursor = connection.cursor()
        cursor.execute(sql)
        coComUser = cursor.fetchone()
        cursor.close()
        if coComUser:
            # print (coComUser[0][1])
            request.session["userName"] = coComUser[1]
            request.session['userId'] = coComUser[0]
            request.session['userPwd'] = coComUser[2]
            return HttpResponseRedirect('../UserControl/')  # HttpResponseRedirect这是执行条件的
        else:
            return render_to_response('login.jsp', {'list': '用户名或者密码错误', })
    else:
        return render_to_response('login.jsp', {'list': '用户名或者密码不能为空', })


# 注册
@csrf_exempt
def IndexEnroll(request):
    if request.method == 'GET':
        return render_to_response('register.jsp')
    else:
        userName = request.POST.get('userName')  # 用户帐号
        userPwd = request.POST.get('userPwd')  # 用户密码
        deptName = request.POST.get('deptName')  # 企业名称
        deptType = request.POST.get('deptType')  # 企业类型
        resType = request.POST.get('resType')  # 资源类别
        mgtMode = request.POST.get('mgtMode')  # 经营模式
        crtDate = request.POST.get('crtDate')  # 成立时间
        peopNum = request.POST.get('peopNum')  # 公司人数
        brandName = request.POST.get('brandName')  # 品牌名称
        mngType = request.POST.get('mngType')  # 管理体系认证
        manMkt = request.POST.get('manMkt')  # 主要市场
        deptAddr = request.POST.get('deptAddr')  # 公司地址
        artPerson = request.POST.get('artPerson')  # 法人
        principalName = request.POST.get('principalName')  # 负责人姓名
        principalTel = request.POST.get('principalTel')  # 负责人电话
        principalMtel = request.POST.get('principalMtel')  # 负责人手机
        businessNo = request.POST.get('businessNo')  # 营业执照号
        regAddr = request.POST.get('regAddr')  # 注册地址
        taxRegNo = request.POST.get('taxRegNo')  # 税务登记号
        deptBrief = request.POST.get('deptBrief')  # 企业简介
        creditLevel = request.POST.get('creditLevel')  # 信用等级
        email1 = request.POST.get('email1')  # 邮件地址
        # 先插入User表 然后插入合作伙伴表
        sqlUser = "INSERT INTO vomodel_cocomuser(userName,userPwd,email,status) VALUES(%s,%s,%s,'Y')"
        sqlUserSelect = "SELECT * FROM vomodel_cocomuser WHERE userName=%s AND userPwd=%s"
        sqlUserSelectOne = "SELECT * FROM vomodel_cocomuser WHERE userName=%s"
        sqlCoPtnrInf = "INSERT INTO vomodel_coptnrinf(userId_id,deptName,deptType,resType,mgtMode,crtDate,peopNum,brandName,mngType,manMkt,deptAddr,artPerson,principalName,principalTel,principalMtel,businessNo,regAddr,taxRegNo,deptBrief,coLevel,creditLevel,status,opStatus,regDate) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'审核中','deptName',%s)"
        cursor = connection.cursor()
        cursor.execute(sqlUserSelectOne, [userName])
        User = cursor.fetchone()
        if not User:
            start = cursor.execute(sqlUser, [userName, userPwd, email1])
            transaction.commit_unless_managed()
            if start == 1:
                cursor.execute(sqlUserSelect, [userName, userPwd])
                User = cursor.fetchone()
                if User:
                    print User
                    userId = User[0]
                    print userId
                    cursor.execute(sqlCoPtnrInf,
                                   [userId, deptName, deptType, resType, mgtMode, crtDate, peopNum, brandName, mngType,
                                    manMkt, deptAddr, artPerson, principalName, principalTel, principalMtel, businessNo,
                                    regAddr, taxRegNo, deptBrief, creditLevel, creditLevel, crtDate])
                    transaction.commit_unless_managed()
                    return HttpResponseRedirect('../')
        else:
            return render_to_response('register.jsp', {'test': '用户存在'})


# 登录后台页面跳转
def UserControl(request):
    userName = request.session.get('userName')
    userId = request.session.get('userId')
    return render(request, 'index.html', {'userName': userName, 'userId': userId})


# 退出页面跳转
# @check_login
def QuitControl(request):
    # del request.session.get['userName']
    request.session.clear()
    return HttpResponseRedirect('../')


# ---------------------------------------------------------完美分割线 前面是登录用的--------------------------------------------------------------------------

# 首页代码
def HomeControl(request):
    return render(request, 'main/code.html')


# 招募信息
def TopnavControl(request):
    sql = 'SELECT * FROM vomodel_coinvtinf'
    cursor = connection.cursor()
    cursor.execute(sql)
    CoInvtInf = cursor.fetchall()
    print CoInvtInf
    return render(request, 'main/menu.html', {'CoInvtInf': CoInvtInf})


# 相应信息
def RigthHomeControl(request):
    datetime.datetime.now().strftime("%Y-%m-%d %H:%I:%S")  # 获取当前时间
    # sqlUserName = 'SELECT * FROM vomodel_cocomuser WHERE userName=%s'
    # insertSql = "insert into vomodel_cocomuser values(%s,%s,%s,'Y')"  # 'aaa','123','543393735@qq.com','Y'
    # selectUserIdSql = 'SELECT * FROM vomodel_cocomuser WHERE userName=%s AND userPwd=%s'
    # # insert = 'insert into co_ptnr_inf values(1,'华为集团','电子产品','电子电子电子','全天','1999-9-9','999','华为','ISO认证','中国','深圳','张三','里斯','110','11124755','49889','中国','11111','简介捷安杰','普通层','基本层级','审核通过','huawei','1999-9-9')'
    sql = 'SELECT * FROM vomodel_CoInvtResponse c JOIN vomodel_coinvtinf p ON c.respId =p.invtId'
    cursor = connection.cursor()
    cursor.execute(sql)
    CoInvtResponse = cursor.fetchall()
    cursor.close()
    return render(request, 'main/second-menu.html', {'CoInvtResponse': CoInvtResponse})


# 工单信息
def SuperfishControl(request):
    sql = 'SELECT * FROM vomodel_CoWformInf w JOIN vomodel_cocomuser u ON w.createUserId_id = u.userId'
    cursor = connection.cursor()
    cursor.execute(sql)
    CoWformInf = cursor.fetchall()
    cursor.close()
    return render(request, 'main/dyna-menu.html', {'CoWformInf': CoWformInf})


# ---------------------页面操作------------------------------
# 用户积分
def OperationControl(request):
    sql = 'SELECT * FROM vomodel_cocomuser u JOIN vomodel_cointegral f ON u.userId = f.ptnrId_id'
    cursor = connection.cursor()
    cursor.execute(sql)
    coComUser = cursor.fetchall()
    cursor.close()
    # for item in coComUser:

    # print coComUser
    coComUsers = []
    for item in coComUser:
        coComUserOne = {}
        coComUserOne['userId'] = item[0]
        coComUserOne['userName'] = item[1]
        coComUserOne['score'] = item[6]
        coComUsers.append(coComUserOne)
    print coComUsers
    return render(request, 'main/operation.html', {'coComUser': coComUsers})


# 获取积分
def QuickControl(request):
    return render(request, 'main/quick.html')


# -----------------------登录控制------------------------------
# 修改密码
@csrf_exempt
def ResourceControl(request):
    if request.method == 'GET':
        userName = request.session.get('userName')
        userId = request.session.get('userId')
        userPwd = request.session.get('userPwd')
        print userPwd
        return render(request, 'main/resource.html', {'userName': userName, 'userId': userId, 'userPwd': userPwd})
    else:
        userPwd = request.POST.get('userPwd')
        userId = request.session.get('userId')
        sql = "UPDATE vomodel_cocomuser SET userPwd =%s  WHERE userId=%s"
        # sql = "INSERT INTO vomodel_cocomuser(userName,userPwd) VALUES(%s,%s)"
        print sql
        cursor = connection.cursor()
        test = cursor.execute(sql, [userPwd, userId])
        transaction.commit_unless_managed()
        if test == 1:
            return render(request, 'form/success.html')
        return render(request, 'form/fail.html')


# 修改用户信息
def LoaderControl(request):
    return render(request, 'main/loader.html')
