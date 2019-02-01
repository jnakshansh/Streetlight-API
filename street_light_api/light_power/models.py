from django.db import models
from datetime import datetime
# Create your models here.
class power(models.Model):
    # id = models.IntegerField(primary_key=True)
    power_consumption = models.IntegerField()
    date_time_record = models.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    def __str__(self):
        return str(self.power_consumption)
