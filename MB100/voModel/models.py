# coding:utf-8
from django.db import models


# Create your models here.


class CoSlctList(models.Model):
    # // 选验列表
    slctId = models.AutoField(primary_key=True)

    subject = models.CharField(max_length=50, null=True)  # 主题

    createUserId = models.CharField(max_length=50, null=True)  # 创建人

    createDate = models.DateTimeField(max_length=50, null=True)  # 创建时间

    belongYear = models.CharField(max_length=50, null=True)  # 归属年

    belongMonth = models.CharField(max_length=50, null=True)  # 归属月

    opFlag = models.CharField(max_length=50, null=True)  # 操作标志


class CoComUser(models.Model):
    # // 用户表
    userId = models.AutoField(primary_key=True)  # 用户编号
    userName = models.CharField(max_length=50, null=True)  # 用户名
    userPwd = models.CharField(max_length=50, null=True)  # 用户密码
    email = models.EmailField(max_length=50, null=True)  # 邮件地址
    status = models.CharField(max_length=50, null=True)  # 状态


class CoIntegral(models.Model):
    # 用户积分
    id = models.AutoField(primary_key=True)
    ptnrId = models.ForeignKey(CoComUser, related_name='ptnrIdHZ')  # 用户外键
    score = models.FloatField(max_length=30, null=True)
    deptName = models.CharField(max_length=50, null=True)
    sort = models.IntegerField(null=True)


class CoPtnrInf(models.Model):
    # 合作伙伴
    spId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(CoComUser, related_name='userIdHZ')

    deptName = models.CharField(max_length=50, null=True)
    deptType = models.CharField(max_length=50, null=True)

    resType = models.CharField(max_length=50, null=True)

    mgtMode = models.CharField(max_length=50, null=True)

    crtDate = models.CharField(max_length=50, null=True)
    peopNum = models.CharField(max_length=50, null=True)

    brandName = models.CharField(max_length=50, null=True)

    mngType = models.CharField(max_length=50, null=True)

    manMkt = models.CharField(max_length=50, null=True)
    deptAddr = models.CharField(max_length=50, null=True)
    artPerson = models.CharField(max_length=50, null=True)

    principalName = models.CharField(max_length=50, null=True)
    principalTel = models.CharField(max_length=50, null=True)

    principalMtel = models.CharField(max_length=50, null=True)

    businessNo = models.CharField(max_length=50, null=True)

    regAddr = models.CharField(max_length=50, null=True)

    taxRegNo = models.CharField(max_length=50, null=True)

    deptBrief = models.CharField(max_length=50, null=True)

    coLevel = models.CharField(max_length=50, null=True)

    creditLevel = models.CharField(max_length=50, null=True)

    status = models.CharField(max_length=50, null=True)

    opStatus = models.CharField(max_length=50, null=True)

    regDate = models.CharField(max_length=50, null=True)
    tian = models.IntegerField(null=True)
    sisi = models.IntegerField(null=True)
    username = models.CharField(max_length=50, null=True)
    userpwd = models.CharField(max_length=50, null=True)
    score = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)


class CoSlctSchema(models.Model):
    # 选验方案
    schemaId = models.AutoField(primary_key=True)

    slctListId = models.ForeignKey(CoSlctList, related_name='slctListId')  # 选验列表ID

    ptnrId = models.ForeignKey(CoPtnrInf, related_name='ptnrIdCS')  # 合作伙伴ID

    schemaName = models.CharField(max_length=500, null=True)  # 方案名称

    schemaDesc = models.CharField(max_length=300, null=True)  # 方案描述

    createDate = models.DateTimeField(null=True)  # 创建时间

    summing = models.CharField(max_length=50, null=True)  # 结论

    dealStatus = models.CharField(max_length=50, null=True)  # 处理状态

    slctType = models.CharField(max_length=50, null=True)  # 选验类型

    attachment = models.FileField(max_length=50, null=True)  # 方案附件

    opStatus = models.FileField(max_length=10, null=True)  # 操作标志


class CoInvtInf(models.Model):
    # 招募信息
    invtId = models.AutoField(primary_key=True)
    rcSubject = models.CharField(max_length=50, null=True)
    resSort = models.CharField(max_length=50, null=True)
    startTime = models.CharField(max_length=50, null=True)
    rcTime = models.CharField(max_length=50, null=True)
    mnTudget = models.CharField(max_length=50, null=True)
    rcNum = models.CharField(max_length=50, null=True)
    rcIntro = models.CharField(max_length=50, null=True)
    faceWay = models.CharField(max_length=50, null=True)
    rcCriterion = models.CharField(max_length=50, null=True)
    advertObject = models.CharField(max_length=50, null=True)
    rcType = models.CharField(max_length=50, null=True)
    units = models.CharField(max_length=50, null=True)
    creatorId = models.CharField(max_length=50, null=True)
    endFlag = models.CharField(max_length=50, null=True)
    opStatus = models.CharField(max_length=50, null=True)
    endDate = models.CharField(max_length=50, null=True)
    runUnit = models.CharField(max_length=50, null=True)
    result = models.IntegerField(null=True, default=0)


class CoInvtResponse(models.Model):
    # 相应招募信息
    respId = models.AutoField(primary_key=True)
    rcId = models.ForeignKey(CoInvtInf, related_name='rcId')

    ptnrId = models.ForeignKey(CoPtnrInf, related_name='ptnrIdCI')

    runUnit = models.CharField(max_length=50, null=True)

    linkman = models.CharField(max_length=50, null=True)

    mobile = models.CharField(max_length=50, null=True)

    email = models.CharField(max_length=50, null=True)

    price = models.CharField(max_length=50, null=True)

    responseStatus = models.CharField(max_length=50, null=True)

    rcStatus = models.CharField(max_length=50, null=True)

    schemaDesc = models.CharField(max_length=50, null=True)

    reason = models.CharField(max_length=50, null=True)

    submitDate = models.CharField(max_length=50, null=True)

    result = models.CharField(max_length=50, null=True)

    attachment = models.CharField(max_length=50, null=True)

    opFlag = models.CharField(max_length=50, null=True)
    rcSubject = models.CharField(max_length=50, null=True)
    deptName = models.CharField(max_length=50, null=True)


class CoDbinfCategory(models.Model):
    # 资讯分类表
    cateId = models.AutoField(primary_key=True)
    cdcName = models.CharField(max_length=50, null=True)
    intro = models.CharField(max_length=50, null=True)


class CoDbinfInfo(models.Model):
    # 资讯信息表
    infoId = models.AutoField(primary_key=True)
    coId = models.ForeignKey(CoDbinfCategory, related_name='coId')
    createorId = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    keyword = models.CharField(max_length=50, null=True)
    cdfContent = models.CharField(max_length=50, null=True)
    createDate = models.CharField(max_length=50, null=True)


class CoComData(models.Model):
    # 资源类别
    dataId = models.AutoField(primary_key=True)
    dataName = models.CharField(max_length=50, null=True)
    dataDescription = models.CharField(max_length=50, null=True)


class SysAdmin(models.Model):
    # 后台登录
    adminId = models.AutoField(primary_key=True)
    adminName = models.CharField(max_length=50, null=True)
    adminPwd = models.CharField(max_length=50, null=True)


class CoWformInf(models.Model):
    # // 工单信息

    wfId = models.AutoField(primary_key=True)  # id
    cwiName = models.CharField(max_length=50, null=True)  # 工单名称
    cwiType = models.CharField(max_length=50, null=True)  # 工单类别
    grade = models.CharField(max_length=50, null=True)  # 级别
    timeLimt = models.CharField(max_length=50, null=True)  # 时间限制
    sendTo = models.CharField(max_length=50, null=True)  # 发送对象
    createDate = models.CharField(max_length=50, null=True)  # 创建时间
    createUserId = models.ForeignKey(CoComUser, related_name='createUserId')  # 创建人
    cwiContent = models.CharField(max_length=50, null=True)  # 内容
    status = models.CharField(max_length=50, null=True)  # 工作状态
    statu = models.CharField(max_length=50, null=True)  #


class CoWformFdbk(models.Model):
    # 工单反馈
    wfkId = models.AutoField(primary_key=True)
    wformId = models.ForeignKey(CoWformInf, related_name='wformId')
    cyfContent = models.CharField(max_length=50, null=True)
    replyId = models.CharField(max_length=50)

