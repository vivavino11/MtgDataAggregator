from dataclasses import dataclass


@dataclass
class Card:
    card_id: int = -1
    name: str = None
    edition: str = None
    condition: str = None
    is_foil: bool = False
