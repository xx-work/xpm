# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-05-14 14:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20190428_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='_private_key',
            field=models.TextField(blank=True, max_length=4096, null=True, verbose_name='SSH private key'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='_public_key',
            field=models.TextField(blank=True, max_length=4096, verbose_name='SSH public key'),
        ),
    ]
