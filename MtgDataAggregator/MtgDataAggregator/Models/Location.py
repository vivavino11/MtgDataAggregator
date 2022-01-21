from dataclasses import dataclass


@dataclass
class Location:
    location_id: int = -1
    name: str = None
    description: str = ""
