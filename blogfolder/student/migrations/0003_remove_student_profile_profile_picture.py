# Generated by Django 5.1.1 on 2024-10-18 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0002_remove_program_course_program_courses"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student_profile",
            name="profile_picture",
        ),
    ]
