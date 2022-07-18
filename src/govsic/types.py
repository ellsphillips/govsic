from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple, Union

SICCode = Union[str, int]


@dataclass
class Section:
    domain: Tuple[int, int]
    description: str
    long_description: str


class Component(Enum):
    SECTION = auto()
    DIVISION = auto()
    GROUP = auto()
    CLASS = auto()
    SUBCLASS = auto()
