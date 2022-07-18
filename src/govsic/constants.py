import string
from typing import List

from govsic.data.glossary import SIC_GLOSSARY
from govsic.data.sections import SECTIONS

DORMANT: int = 99999

BINS: List[int] = [s.domain[0] for s in SECTIONS.values()]

LETTERS: List[str] = list(string.ascii_uppercase[:21])

CODES: List[str] = list(SIC_GLOSSARY)
