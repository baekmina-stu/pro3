# Generated by Django 4.2.2 on 2023-06-13 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articleapp", "0004_category_remove_article_image_article_hits_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Category",
        ),
    ]