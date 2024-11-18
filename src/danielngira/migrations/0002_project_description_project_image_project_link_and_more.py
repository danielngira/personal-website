# Generated by Django 4.2.5 on 2024-06-09 04:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("danielngira", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="image",
            field=models.ImageField(
                default="static/danielngira/images/placeholderimage.jpg", upload_to=""
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="link",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="name",
            field=models.TextField(blank=True, null=True),
        ),
    ]