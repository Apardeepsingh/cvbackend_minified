# Generated by Django 4.2.4 on 2023-08-18 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_alter_project_websitelink'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_background_color',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_background_image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_border_color',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]