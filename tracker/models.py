from django.db import models

class Device(models.Model):
    device_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_id

class CallLogEntry(models.Model):
    device = models.ForeignKey(Device, related_name="call_logs", on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    call_type = models.CharField(max_length=50)
    duration = models.IntegerField(default=0)
    timestamp = models.BigIntegerField()  # Unix timestamp in ms

class LocationEntry(models.Model):
    device = models.ForeignKey(Device, related_name="locations", on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()
