# Generated by Django 5.0 on 2024-10-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0017_alter_student_status_alter_student_student_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student_profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="student_profile"),
        ),
    ]
