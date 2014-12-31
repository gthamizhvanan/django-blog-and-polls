# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logmindblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lmblog',
            old_name='subtitle',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='lmcategory',
            old_name='catSlug',
            new_name='slug',
        ),
    ]
