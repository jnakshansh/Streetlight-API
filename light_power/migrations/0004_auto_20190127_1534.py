# Generated by Django 2.1.2 on 2019-01-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_power', '0003_auto_20190126_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power',
            name='date_time_record',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
