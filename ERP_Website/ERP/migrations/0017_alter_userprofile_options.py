# Generated by Django 4.2.5 on 2023-10-20 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0016_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['user']},
        ),
    ]
