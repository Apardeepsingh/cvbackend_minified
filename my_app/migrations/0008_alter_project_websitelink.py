# Generated by Django 4.2.4 on 2023-08-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_project_project_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='websiteLink',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
