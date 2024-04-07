# encoding=utf-8
# Generated by Django 3.2.23 on 2024-01-31 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0004_auto_20240131_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': '功能板块'},
        ),
        migrations.RemoveField(
            model_name='module',
            name='child',
        ),
        migrations.AddField(
            model_name='module',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单图标'),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='module',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='菜单排列次序'),
        ),
        migrations.CreateModel(
            name='SubModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.CharField(blank=True, max_length=255, null=True, verbose_name='二级菜单')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='描述')),
                ('frontpath', models.TextField(blank=True, max_length=1000, null=True, verbose_name='前端路由')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单图标')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='菜单排列次序')),
                ('menus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='module.module', verbose_name='一级菜单')),
            ],
            options={
                'verbose_name': '二级菜单',
                'db_table': 'modules_sub',
                'permissions': [('can_get', '用户或组可获取该菜单')],
            },
        ),
    ]