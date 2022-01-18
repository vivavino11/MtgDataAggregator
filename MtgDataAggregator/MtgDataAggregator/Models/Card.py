from dataclasses import dataclass


@dataclass
class Card:
    name: str
    edition: str
    condition: str
    is_foil: bool
