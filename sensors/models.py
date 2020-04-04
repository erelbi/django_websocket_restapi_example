from django.db import models

"""Veritabanı Tablo modellerini burda oluşturduk"""
class SensorA(models.Model):
    ram_usage = models.CharField(max_length=20)
    cpu_freq = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.value

class SensorB(models.Model):
     value = models.CharField(max_length=20)
     client = models.CharField(max_length=20)
     time = models.DateTimeField(auto_now_add=True)