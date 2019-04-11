# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-06 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20180704_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='UserProFilebg/avatar/%y/%d/07013906f8134e71bbfcfe6d9ef03cea'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, default='/default/default.jpg', null=True, upload_to='UserProFilebg/%Y/%m/07013906f8134e71bbfcfe6d9ef03cea', verbose_name='背景图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_bh',
            field=models.CharField(default='4dc8444ff1e545568dd2f6b8cde746c9', max_length=50, unique=True, verbose_name='用户唯一ID'),
        ),
    ]
