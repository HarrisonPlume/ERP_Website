# Generated by Django 4.2.5 on 2023-10-20 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0019_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
