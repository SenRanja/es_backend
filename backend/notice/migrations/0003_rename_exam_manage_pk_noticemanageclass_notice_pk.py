# encoding=utf-8
# Generated by Django 3.2.23 on 2024-02-22 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_noticemanageclass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticemanageclass',
            old_name='exam_manage_pk',
            new_name='notice_pk',
        ),
    ]