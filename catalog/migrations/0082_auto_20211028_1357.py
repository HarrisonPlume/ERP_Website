# Generated by Django 3.2.5 on 2021-10-28 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0081_auto_20211028_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='header_plate_task',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='header_plate_task',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
