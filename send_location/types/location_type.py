from pydantic import BaseModel

class LocationInterface(BaseModel):
    """location interface
    """
    device_id: str
    lat: str
    lon: str
    speed: str