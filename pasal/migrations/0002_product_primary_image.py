# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pasal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='primary_image',
            field=models.ImageField(upload_to='Images', default=datetime.datetime(2015, 9, 30, 6, 16, 20, 535404, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
