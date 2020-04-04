from rest_framework import serializers
from sensors.models import SensorB, SensorA

class  SensorASerilazer(serializers.ModelSerializer):
    def create(self, validated_data):
        return SensorA.objects.create(**validated_data)
    class Meta:
        model = SensorA
        fields = [
            "ram_usage","cpu_freq",
        ]

# class   SensorBSerilazer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     client = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return SensorB.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.client = validated_data.get('client', instance.client)
#         instance.sensor = validated_data.get('sensor', instance.sensor)
#         instance.date = validated_data.get('date', instance)
#         instance.save()
#         return instance
#
# class SensorB(serializers.ModelSerializer):
#     class Meta:
#         model = SensorB
#         fields = ['client', 'sensor', 'date']