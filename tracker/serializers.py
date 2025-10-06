from rest_framework import serializers

class CallLogEntrySerializer(serializers.Serializer):
    number = serializers.CharField()
    type = serializers.CharField()  # matches Flutter's 'type'
    duration = serializers.IntegerField()
    timestamp = serializers.IntegerField()

class LocationEntrySerializer(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    # remove timestamp from location; use parent timestamp instead

class DeviceDataSerializer(serializers.Serializer):
    device_id = serializers.CharField()
    timestamp = serializers.DateTimeField()
    location = LocationEntrySerializer()
    call_logs = CallLogEntrySerializer(many=True)
