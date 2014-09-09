# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('short', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=200)),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('target', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=200)),
                ('coefficient', models.FloatField(default=1)),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('sourceUnit', models.ForeignKey(related_name=b'UnitRelation.sourceUnit', to='converter.BUnit')),
                ('targetUnit', models.ForeignKey(related_name=b'UnitRelation.targetUnit', to='converter.BUnit')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitRelationChain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('coefficient', models.FloatField(default=1)),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('sourceUnit', models.ForeignKey(related_name=b'sourceUnit', to='converter.BUnit')),
                ('targetUnit', models.ForeignKey(related_name=b'targetUnit', to='converter.BUnit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitRelationChainItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(default=0)),
                ('chain', models.ForeignKey(to='converter.UnitRelationChain')),
                ('relation', models.ForeignKey(to='converter.UnitRelation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='chain',
            field=models.ForeignKey(to='converter.UnitRelationChain'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='relateTo',
            field=models.ForeignKey(to='converter.Comment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='relation',
            field=models.ForeignKey(to='converter.UnitRelation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='unit',
            field=models.ForeignKey(to='converter.BUnit'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
