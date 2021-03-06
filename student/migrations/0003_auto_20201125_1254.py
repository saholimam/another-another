# Generated by Django 3.1.3 on 2020-11-25 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='photo',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='student',
            name='reg',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(unique=True),
        ),
    ]
