# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20160126_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='about',
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_item',
        ),
        migrations.AddField(
            model_name='category',
            name='full_about',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='min_count',
            field=models.IntegerField(default=0, verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AddField(
            model_name='category',
            name='price_from',
            field=models.IntegerField(default=0, verbose_name='\u0426\u0435\u043d\u0430 \u043e\u0442'),
        ),
        migrations.AddField(
            model_name='category',
            name='price_to',
            field=models.IntegerField(default=0, verbose_name='\u0426\u0435\u043d\u0430 \u0434\u043e'),
        ),
        migrations.AddField(
            model_name='category',
            name='short_about',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='category',
            name='utm',
            field=models.CharField(default='', max_length=255, verbose_name='UTM \u043c\u0435\u0442\u043a\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='full_about',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='item',
            name='min_count',
            field=models.IntegerField(default=0, verbose_name='\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e'),
        ),
        migrations.AddField(
            model_name='item',
            name='short_about',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
    ]
