# Generated by Django 3.2.5 on 2021-07-07 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210707_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component_PrepTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Component_Prep_Tasks',
        ),
    ]