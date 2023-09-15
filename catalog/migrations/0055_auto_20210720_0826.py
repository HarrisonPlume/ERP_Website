# Generated by Django 3.2.5 on 2021-07-19 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0054_part_plating_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentpreptaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('z', 'Complete'), ('b', 'In Progress'), ('f', 'Failed')], default='a', help_text='Set                                   task completion status', max_length=1),
        ),
        migrations.AlterField(
            model_name='deburrtaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('z', 'Complete'), ('b', 'In Progress'), ('f', 'Failed')], default='a', help_text='Set task completion status', max_length=1),
        ),
        migrations.AlterField(
            model_name='formingtaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('z', 'Complete'), ('b', 'In Progress'), ('f', 'Failed')], default='a', help_text='Set task completion status', max_length=1),
        ),
        migrations.AlterField(
            model_name='headerplatetaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('z', 'Complete'), ('b', 'In Progress'), ('f', 'Failed')], default='a', help_text='Set                                   task completion status', max_length=1),
        ),
        migrations.AlterField(
            model_name='pitchingtaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('z', 'Complete'), ('b', 'In Progress'), ('f', 'Failed')], default='a', help_text='Set task completion status', max_length=1),
        ),
        migrations.AlterField(
            model_name='platingtaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('z', 'Complete'), ('b', 'In Progress'), ('f', 'Failed')], default='a', help_text='Set task completion status', max_length=1),
        ),
        migrations.AlterField(
            model_name='stackingtaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('z', 'Complete'), ('b', 'In Progress'), ('f', 'Failed')], default='a', help_text='Set                                   task completion status', max_length=1),
        ),
        migrations.AlterField(
            model_name='wirecuttaskinstance',
            name='status',
            field=models.CharField(choices=[('a', 'Not Started'), ('h', 'On Hold'), ('z', 'Complete'), ('b', 'In Progress'), ('f', 'Failed')], default='a', help_text='Set task completion status', max_length=1),
        ),
    ]
