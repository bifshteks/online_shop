# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='date_pub',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
