# Generated by Django 5.0.4 on 2024-04-25 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_userregister_registeruser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RegisterUser',
            new_name='User',
        ),
    ]
