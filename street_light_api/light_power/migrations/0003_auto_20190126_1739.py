# Generated by Django 2.1.2 on 2019-01-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_power', '0002_auto_20190126_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power',
            name='date_time_record',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='power',
            name='power_consumption',
            field=models.IntegerField(),
        ),
    ]