# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-04-03 22:20
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations
from django.db import models

import kolibri.core.discovery.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("discovery", "0006_networklocation_min_content_schema_version"),
    ]

    operations = [
        migrations.CreateModel(
            name="PinnedDevice",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=kolibri.core.discovery.models._uuid_string,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("instance_id", models.UUIDField()),
                (
                    "created",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="pinneddevice",
            unique_together=set([("user", "instance_id")]),
        ),
    ]