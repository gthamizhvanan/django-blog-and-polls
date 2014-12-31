# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lmBlog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('blogtitle', models.CharField(max_length=100, unique=True)),
                ('subtitle', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('posteddate', models.DateField(db_index=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='lmCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('catTitle', models.CharField(max_length=100, unique=True)),
                ('catSlug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lmblog',
            name='blogcategory',
            field=models.ForeignKey(to='logmindblog.lmCategory'),
            preserve_default=True,
        ),
    ]
