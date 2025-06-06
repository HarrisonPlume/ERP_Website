# Generated by Django 4.2.5 on 2025-04-15 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0029_userprofile_date_of_birth_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(default='noemail@outlook.com', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='post_code',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='postal_address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='prefered_traning',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='ERP.gym_class'),
        ),
    ]
