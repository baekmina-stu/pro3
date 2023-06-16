from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from ckeditor.fields import RichTextField


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("jjit", "0005_remove_question_image_remove_question_like_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="writer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Answer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="like",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="question",
            name="writer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Question",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="content",
            field=RichTextField(null=True),
        ),
    ]
