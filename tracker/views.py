from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Device, CallLogEntry, LocationEntry
from .serializers import DeviceDataSerializer

class UploadDeviceData(APIView):
    def post(self, request, format=None):
        serializer = DeviceDataSerializer(data=request.data)
        if serializer.is_valid():
            device_id = serializer.validated_data['device_id']
            timestamp = serializer.validated_data['timestamp']
            location_data = serializer.validated_data['location']
            call_logs_data = serializer.validated_data['call_logs']

            device, created = Device.objects.get_or_create(device_id=device_id)

            # Save location
            LocationEntry.objects.create(
                device=device,
                latitude=location_data['latitude'],
                longitude=location_data['longitude'],
                timestamp=timestamp  # use parent timestamp
            )

            # Save call logs
            for log in call_logs_data:
                CallLogEntry.objects.create(
                    device=device,
                    number=log['number'],
                    call_type=log['type'],  # matches serializer field
                    duration=log['duration'],
                    timestamp=log['timestamp']
                )

            return Response({"status": "success"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
