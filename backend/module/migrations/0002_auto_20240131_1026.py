# encoding=utf-8
# Generated by Django 3.2.23 on 2024-01-31 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='name',
        ),
        migrations.AddField(
            model_name='module',
            name='child',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='二级菜单'),
        ),
        migrations.AddField(
            model_name='module',
            name='menus',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='一级菜单'),
        ),
    ]