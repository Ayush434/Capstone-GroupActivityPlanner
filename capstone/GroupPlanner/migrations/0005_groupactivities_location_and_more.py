# Generated by Django 4.0.6 on 2022-12-22 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupPlanner', '0004_groupactivities_groupname'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupactivities',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='groupactivities',
            name='meeting_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
