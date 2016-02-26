# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('alt_tag', models.CharField(max_length=255, verbose_name='Alt tag', blank=True)),
                ('text', models.TextField(verbose_name='Descriptive text', blank=True)),
                ('image', filer.fields.image.FilerImageField(related_name='+', verbose_name='Image', to='filer.Image')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GalleryPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='gallerypicture',
            name='plugin',
            field=models.ForeignKey(related_name='pictures', to='cmsplugin_photogallery.GalleryPlugin'),
        ),
    ]
