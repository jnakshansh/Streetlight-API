# Generated by Django 2.1.2 on 2019-02-01 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light_power', '0006_auto_20190201_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='power',
            name='date_time_record',
            field=models.DateTimeField(default='2019-02-01 12:00:19'),
        ),
    ]