# Generated by Django 5.0 on 2024-10-31 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0019_alter_student_profile_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student_profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="student_profile"),
        ),
    ]