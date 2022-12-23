from django.db import models

# Create your models here.


class FurnaceData(models.Model):
    DataTime = models.TimeField()
    data = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.DataTime} data {self.data}"
