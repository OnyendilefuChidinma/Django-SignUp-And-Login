# Generated by Django 5.0 on 2024-11-18 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0023_alter_student_profile_student_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="slug",
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]