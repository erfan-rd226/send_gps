from django.db import transaction

from send_location.models import Location, Device
from send_location.types.location_type import LocationInterface

def update_device(*, location:Location) -> Device:
    """update device last position

    Args:
        location (Location): location object model

    Returns:
        Device: device object model
    """
    device = Device.objects.get(unique_id=location.device_id)
    device.last_position_id=location.id
    device.save()
    return device

@transaction.atomic
def create_location_device(*, location_data:LocationInterface) -> Location:
    """create location device

    Args:
        location_data (LocationInterface): interface location 

    Returns:
        Location: location object model
    """
    location = Location.objects.create(
        device_id=location_data.device_id,
        lat=location_data.lat,
        lon=location_data.lon,
        speed=location_data.speed,
    )

    update_device(location=location)

    return location