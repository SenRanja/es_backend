# encoding=utf-8
from django.urls import path
from testonly import views

urlpatterns = [

    # 公告列表
    path("test_paginator/", views.test_paginator2),

]