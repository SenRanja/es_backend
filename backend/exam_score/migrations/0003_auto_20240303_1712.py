# encoding=utf-8
# Generated by Django 3.2.23 on 2024-03-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_score', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examsubjectiveresult',
            name='sub_obj',
            field=models.CharField(blank=True, choices=[('sub', '主观'), ('obj', '客观')], max_length=10, null=True, verbose_name='主客观'),
        ),
        migrations.AlterModelTable(
            name='examsubjectiveresult',
            table='exam_result_record',
        ),
    ]