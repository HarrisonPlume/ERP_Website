# Generated by Django 3.2.5 on 2021-07-20 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0056_auto_20210720_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='serial',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
