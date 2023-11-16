from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)


class Measurement(models.Model):

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if self.created_at:
    #         self.created_at = models.DateTimeField(auto_now=True)
    #         return super().save()

