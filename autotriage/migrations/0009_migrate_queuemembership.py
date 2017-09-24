# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import migrations
from django.db.utils import IntegrityError
from django.utils.translation import ugettext_lazy as _


def create_and_assign_permissions(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    # Two steps:
    #   1. Create the permission for existing Queues
    #   2. Assign the permission to user according to QueueMembership objects

    # First step: prepare the permission for each queue
    Queue = apps.get_model('autotriage', 'Queue')

    for q in Queue.objects.all():
        if not q.permission_name:
            basename = "queue_access_%s" % q.slug
            q.permission_name = "autotriage.%s" % basename
        else:
            # Strip the `autotriage.` prefix
            basename = q.permission_name[9:]

        try:
            Permission.objects.create(
                name=_("Permission for queue: ") + q.title,
                content_type=ContentType.objects.get(model="queue"),
                codename=basename,
            )
        except IntegrityError:
            # Seems that it already existed, safely ignore it
            pass
        q.save()

    # Second step: map the permissions according to QueueMembership
    QueueMembership = apps.get_model('autotriage', 'QueueMembership')
    for qm in QueueMembership.objects.all():
        user = qm.user
        for q in qm.queues.all():
            # Strip the `autotriage.` prefix
            p = Permission.objects.get(codename=q.permission_name[9:])
            user.user_permissions.add(p)
        qm.delete()


def revert_queue_membership(apps, schema_editor):
    Permission = apps.get_model('auth', 'Permission')
    Queue = apps.get_model('autotriage', 'Queue')
    QueueMembership = apps.get_model('autotriage', 'QueueMembership')
    for p in Permission.objects.all():
        if p.codename.startswith("queue_access_"):
            slug = p.codename[13:]
            try:
                q = Queue.objects.get(slug=slug)
            except ObjectDoesNotExist:
                continue

            for user in p.user_set.all():
                qm, _ = QueueMembership.objects.get_or_create(user=user)
                qm.queues.add(q)

            p.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('autotriage', '0008_extra_for_permissions'),
    ]

    operations = [
        migrations.RunPython(create_and_assign_permissions,
                             revert_queue_membership)
    ]
