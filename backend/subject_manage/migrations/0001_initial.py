# encoding=utf-8
# Generated by Django 3.2.23 on 2024-01-27 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, unique=True, verbose_name='学科名字')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('description', models.TextField(blank=True, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '学科管理',
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='SubjectStaffGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subject_manage.subject', verbose_name='学科')),
            ],
            options={
                'verbose_name': '教师对学科的管理',
                'db_table': 'subjects_staff',
            },
        ),
    ]