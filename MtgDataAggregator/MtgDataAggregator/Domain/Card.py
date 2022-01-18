from dataclasses import dataclass


@dataclass
class Card:
    card_id: int
    collection_id: int
    location_id: int
    name: str
    edition: str
    condition: str
    is_foil: bool
