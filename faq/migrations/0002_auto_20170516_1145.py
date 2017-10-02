# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default='', help_text='Description of topic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='faq-images/topics/'),
        ),
    ]