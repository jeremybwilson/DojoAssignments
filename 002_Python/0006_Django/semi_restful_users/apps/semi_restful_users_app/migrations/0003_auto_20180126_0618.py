# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 06:18
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('semi_restful_users_app', '0002_auto_20180126_0615'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('my_form_validators', django.db.models.manager.Manager()),
            ],
        ),
    ]