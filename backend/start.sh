#!/bin/bash

# 迁移数据
/usr/local/bin/python /app/manage.py makemigrations user video notice question_manage exam_manage exam_score license subject_manage module system_manage system_monitor ftp testonly
/usr/local/bin/python /app/manage.py migrate

# 开启cron定时任务
/etc/init.d/cron restart && /etc/init.d/cron status && /etc/init.d/cron start

# 前台任务，启动django
/usr/local/bin/uwsgi /app/uwsgi.ini