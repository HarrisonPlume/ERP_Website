# Generated by Django 3.2.5 on 2021-07-26 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0073_auto_20210726_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentpreptaskinstance',
            name='serial',
            field=models.CharField(max_length=5, null=True),
        ),
    ]