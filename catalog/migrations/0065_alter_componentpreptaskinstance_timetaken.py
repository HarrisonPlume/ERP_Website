# Generated by Django 3.2.5 on 2021-07-22 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0064_auto_20210721_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentpreptaskinstance',
            name='timetaken',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
