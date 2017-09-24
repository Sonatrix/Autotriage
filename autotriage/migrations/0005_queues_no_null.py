# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autotriage', '0004_add_per_queue_staff_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escalationexclusion',
            name='queues',
            field=models.ManyToManyField(
                help_text='Leave blank for this exclusion to be applied to all queues, or select those queues you wish to exclude with this entry.', to='autotriage.Queue', blank=True),
        ),
        migrations.AlterField(
            model_name='ignoreemail',
            name='queues',
            field=models.ManyToManyField(
                help_text='Leave blank for this e-mail to be ignored on all queues, or select those queues you wish to ignore this e-mail for.', to='autotriage.Queue', blank=True),
        ),
        migrations.AlterField(
            model_name='presetreply',
            name='queues',
            field=models.ManyToManyField(
                help_text='Leave blank to allow this reply to be used for all queues, or select those queues you wish to limit this reply to.', to='autotriage.Queue', blank=True),
        ),
    ]
