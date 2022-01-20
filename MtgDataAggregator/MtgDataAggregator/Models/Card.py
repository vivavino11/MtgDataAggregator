from dataclasses import dataclass


@dataclass
class Card:
    name: str = None
    edition: str = None
    condition: str = None
    is_foil: bool = False