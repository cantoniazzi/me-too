# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contacts',
            field=models.ManyToManyField(to='profiles.Profile', related_name='contacts_rel_+'),
            preserve_default=True,
        ),
    ]
