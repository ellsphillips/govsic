import string
from dataclasses import fields
from enum import Enum, auto
from typing import Dict, List

from govsic.data.glossary import SIC_GLOSSARY
from govsic.data.sections import SECTION

DORMANT: int = 99999

class Component(Enum):
    SECTION = auto()
    DIVISION = auto()
    GROUP = auto()
    CLASS = auto()
    SUBCLASS = auto()


class SectionBoundaries(Enum):
    A = 1000
    B = 5000
    C = 10000
    D = 35000
    E = 36000
    F = 41000
    G = 45000
    H = 49000
    I = 55000
    J = 58000
    K = 64000
    L = 68000
    M = 69000
    N = 77000
    O = 84000
    P = 85000
    Q = 86000
    R = 90000
    S = 94000
    T = 97000
    U = 99000


LETTERS: List[str] = list(string.ascii_uppercase[:21])

ALL_CODES: List[str] = list(SIC_GLOSSARY)

SECTIONS: Dict[str, str] = {
    field.name: getattr(SECTION, field.name).description
    for field in fields(SECTION)
}
