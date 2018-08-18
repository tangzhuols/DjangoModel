# coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from EnterUser import views, InfoZoneViews, PartnerZoneViews, RecruitZoneViews

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MB100.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # -------------------完美分割线-----------------------------
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.index),  # 跳转到登录页面
                       url(r'^enterUsers/$', views.enterUsers),  # 寻址登录 和错误寻址
                       url(r'^UserControl/$', views.UserControl),  # 成功认证跳转
                       url(r'^QuitControl/$', views.QuitControl), # 退出认证跳转
                       url(r'^IndexEnroll/$', views.IndexEnroll),# 注册


                       # ---------------------首页内容------------------------------
                       url(r'^HomeControl/$', views.HomeControl),  # 首页代码
                       url(r'^TopnavControl/$', views.TopnavControl),  # 招募信息
                       url(r'^RigthHomeControl/$', views.RigthHomeControl),  # 相应信息
                       url(r'^SuperfishControl/$', views.SuperfishControl),  # 工单信息

                       # ---------------------页面操作------------------------------
                       url(r'^OperationControl/$', views.OperationControl),  # 页面常见操作
                       url(r'^QuickControl/$', views.QuickControl),  # 页面操作快捷方式

                       # -----------------------文件结构------------------------------
                       url(r'^ResourceControl/$', views.ResourceControl),  # # 资源文件结构
                       url(r'^LoaderControl/$', views.LoaderControl),  # 引入JS方式

                       # ----################################## 招募页的细化 #####################################################----
                       url(r'^RecruitmentOne/$', RecruitZoneViews.RecruitmentOne),  # 单个招募详情
                       )
