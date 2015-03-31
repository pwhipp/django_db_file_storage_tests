# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_uploader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='fileuploader',
            name='upload',
            field=models.FileField(null=True, upload_to=b'file_uploader.DBFile/bytes/filename/mimetype', blank=True),
            preserve_default=True,
        ),
    ]
