# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('utm', models.CharField(max_length=255, verbose_name='UTM \u043c\u0435\u0442\u043a\u0430')),
                ('price_from', models.IntegerField(default=0, verbose_name='\u0426\u0435\u043d\u0430 \u043e\u0442')),
                ('price_to', models.IntegerField(default=0, verbose_name='\u0426\u0435\u043d\u0430 \u0434\u043e')),
                ('about', tinymce.models.HTMLField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('is_item', models.BooleanField(default=False, verbose_name='\u042f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043b\u0438 \u043a\u043e\u043d\u043a\u0440\u0435\u0442\u043d\u044b\u043c \u0442\u043e\u0432\u0430\u0440\u043e\u043c')),
                ('image', models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u0422\u043e\u0432\u0430\u0440',
                'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b',
            },
        ),
    ]
