# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0004_auto_20140909_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageId',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='chain',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='relateTo',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='unitrelation',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='unitrelation',
            name='like',
        ),
        migrations.RemoveField(
            model_name='unitrelationchain',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='unitrelationchain',
            name='like',
        ),
        migrations.AddField(
            model_name='bunit',
            name='page',
            field=models.OneToOneField(null=True, to='converter.PageId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unitrelation',
            name='page',
            field=models.OneToOneField(null=True, to='converter.PageId'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='unitrelationchain',
            name='page',
            field=models.OneToOneField(null=True, to='converter.PageId'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bunit',
            name='user',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='unitrelation',
            name='user',
            field=models.IntegerField(default=0),
        ),
    ]
