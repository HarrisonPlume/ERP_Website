# Generated by Django 3.2.5 on 2021-07-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0044_pitching_task_pitchingtaskinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='Pitching_tasks',
            field=models.ManyToManyField(to='catalog.Pitching_Task'),
        ),
    ]
