# Generated by Django 4.2.1 on 2023-05-21 08:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jjit", "0004_question_like_question_writer_alter_question_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="question",
            name="image",
        ),
        migrations.RemoveField(
            model_name="question",
            name="like",
        ),
        migrations.RemoveField(
            model_name="question",
            name="title",
        ),
        migrations.RemoveField(
            model_name="question",
            name="writer",
        ),
        migrations.AddField(
            model_name="question",
            name="subject",
            field=models.CharField(
                default=datetime.datetime(
                    2023, 5, 21, 8, 40, 12, 451774, tzinfo=datetime.timezone.utc
                ),
                max_length=200,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="question",
            name="content",
            field=models.TextField(
                default=datetime.datetime(
                    2023, 5, 21, 8, 40, 48, 679653, tzinfo=datetime.timezone.utc
                )
            ),
            preserve_default=False,
        ),
    ]
