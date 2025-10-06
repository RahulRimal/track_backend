from django.contrib import admin
from .models import Device, CallLogEntry, LocationEntry

admin.site.register(Device)
# admin.site.register(CallLogEntry)
# admin.site.register(LocationEntry)

@admin.register(CallLogEntry)
class CallLogEntryAdmin(admin.ModelAdmin):
    list_display = ('device', 'number', 'call_type', 'duration', 'timestamp')


@admin.register(LocationEntry)
class LocationEntryAdmin(admin.ModelAdmin):
    list_display = ('device', "latitude", "longitude" , 'timestamp')
    