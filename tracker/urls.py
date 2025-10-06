from django.urls import path
from .views import UploadDeviceData

urlpatterns = [
    path('upload/', UploadDeviceData.as_view(), name='upload-device-data'),
]
