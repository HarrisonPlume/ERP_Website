# Generated by Django 3.2.5 on 2021-07-14 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0051_deburr_task_deburrtaskinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='Deburr_tasks',
            field=models.ManyToManyField(help_text='                                            Select the nessessary deburr                                                tasks', to='catalog.Deburr_Task'),
        ),
    ]