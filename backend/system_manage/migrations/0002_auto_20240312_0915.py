# Generated by Django 3.2.23 on 2024-03-12 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemmanagesetting',
            name='cheat_mouse_out',
            field=models.IntegerField(blank=True, null=True, verbose_name='鼠标移出屏幕次数'),
        ),
        migrations.AddField(
            model_name='systemmanagesetting',
            name='cheat_page_out',
            field=models.IntegerField(blank=True, null=True, verbose_name='切屏次数'),
        ),
    ]