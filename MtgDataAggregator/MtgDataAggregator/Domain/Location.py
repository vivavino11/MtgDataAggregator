from dataclasses import dataclass


@dataclass
class Location:
    location_id: int
    collection_id: int
    name: str
    description: str
