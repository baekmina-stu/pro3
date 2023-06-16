import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("articleapp", "0003_article_like"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("has_answer", models.BooleanField(default=True)),
            ],
        ),
        # Commenting out the following lines to remove the create model operation
        # migrations.RemoveField(
        #     model_name="article",
        #     name="image",
        # ),
        # migrations.AddField(
        #     model_name="article",
        #     name="hits",
        #     field=models.PositiveIntegerField(default=1, verbose_name="조회수"),
        # ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                blank=True, null=True
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
