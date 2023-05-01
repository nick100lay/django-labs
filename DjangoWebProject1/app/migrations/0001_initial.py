# Generated by Django 4.1.7 on 2023-04-24 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100,
                        unique_for_date="posted",
                        verbose_name="Заголоnок",
                    ),
                ),
                ("description", models.TextField(verbose_name="Краткoе содержание")),
                ("content", models.TextField(verbose_name="Полное содернание")),
                (
                    "posted",
                    models.DateTimeField(
                        db_index=True,
                        default=datetime.datetime(2023, 4, 24, 12, 32, 31, 570416),
                        verbose_name="Опубликована",
                    ),
                ),
            ],
            options={
                "verbose_name": "статья блога",
                "verbose_name_plural": "статьи блогa",
                "db_table": "Posts",
                "ordering": ["-posted"],
            },
        ),
    ]
