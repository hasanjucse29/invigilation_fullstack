# Generated by Django 3.0.8 on 2021-01-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_feed_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='head',
            name='heading',
            field=models.CharField(default='EXAM TIMETABLE', max_length=1000),
        ),
        migrations.AlterField(
            model_name='tt',
            name='Branch',
            field=models.CharField(choices=[('it', 'information technology'), ('eee', 'electrical'), ('cse', 'computer science'), ('ece', 'electronics and communication')], max_length=5),
        ),
    ]
