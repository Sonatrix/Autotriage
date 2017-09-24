# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-08 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autotriage', '0015_expand_permission_name_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'ordering': ('filename',), 'verbose_name': 'Attachment', 'verbose_name_plural': 'Attachments'},
        ),
        migrations.AlterModelOptions(
            name='emailtemplate',
            options={'ordering': ('template_name', 'locale'), 'verbose_name': 'e-mail template', 'verbose_name_plural': 'e-mail templates'},
        ),
        migrations.AlterModelOptions(
            name='followup',
            options={'ordering': ('date',), 'verbose_name': 'Follow-up', 'verbose_name_plural': 'Follow-ups'},
        ),
        migrations.AlterModelOptions(
            name='kbcategory',
            options={'ordering': ('title',), 'verbose_name': 'Knowledge base category', 'verbose_name_plural': 'Knowledge base categories'},
        ),
        migrations.AlterModelOptions(
            name='kbitem',
            options={'ordering': ('title',), 'verbose_name': 'Knowledge base item', 'verbose_name_plural': 'Knowledge base items'},
        ),
        migrations.AlterModelOptions(
            name='presetreply',
            options={'ordering': ('name',), 'verbose_name': 'Pre-set reply', 'verbose_name_plural': 'Pre-set replies'},
        ),
        migrations.AlterUniqueTogether(
            name='ticketcustomfieldvalue',
            unique_together=set([('ticket', 'field')]),
        ),
    ]