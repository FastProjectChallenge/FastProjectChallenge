# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_auto_20140909_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunit',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='chain',
            field=models.ForeignKey(to='converter.UnitRelationChain', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='relateTo',
            field=models.ForeignKey(to='converter.Comment', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='relation',
            field=models.ForeignKey(to='converter.UnitRelation', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unit',
            field=models.ForeignKey(to='converter.BUnit', null=True),
        ),
        migrations.AlterField(
            model_name='unitrelation',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
