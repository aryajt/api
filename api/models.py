# api/models.py
from django.db import models

class Device(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    deviceModel = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    note = models.TextField()
    serial = models.CharField(max_length=50)

    def __str__(self):
        return self.name