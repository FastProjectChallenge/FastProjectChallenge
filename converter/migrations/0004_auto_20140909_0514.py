# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_auto_20140909_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunit',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='chain',
            field=models.ForeignKey(default=None, blank=True, to='converter.UnitRelationChain', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='relateTo',
            field=models.ForeignKey(default=None, blank=True, to='converter.Comment', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='relation',
            field=models.ForeignKey(default=None, blank=True, to='converter.UnitRelation', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unit',
            field=models.ForeignKey(default=None, blank=True, to='converter.BUnit', null=True),
        ),
        migrations.AlterField(
            model_name='unitrelation',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'', blank=True),
        ),
    ]
