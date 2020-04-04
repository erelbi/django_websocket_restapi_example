from sensors.models import SensorA
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=SensorA)
def sensor_info(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "sensors", {"type": "sensors",
                       "event": "CpuMem",
                       "mem": instance.ram_usage,
                        "cpu": instance.cpu_freq})