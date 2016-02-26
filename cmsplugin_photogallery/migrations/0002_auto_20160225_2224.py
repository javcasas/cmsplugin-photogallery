# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_photogallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryplugin',
            name='cell_class',
            field=models.CharField(default=b'col-xs-12 col-sm-6 col-lg-4', max_length=255, verbose_name='Cell CSS Class', blank=True),
        ),
        migrations.AddField(
            model_name='galleryplugin',
            name='img_class',
            field=models.CharField(default=b'col-xs-12', max_length=255, verbose_name='Img CSS Class', blank=True),
        ),
        migrations.AddField(
            model_name='galleryplugin',
            name='items_per_row',
            field=models.PositiveIntegerField(default=3, verbose_name='Images per row'),
        ),
        migrations.AddField(
            model_name='galleryplugin',
            name='row_class',
            field=models.CharField(default=b'col-xs-12', max_length=255, verbose_name='Row CSS Class', blank=True),
        ),
    ]
