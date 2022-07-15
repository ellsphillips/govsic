import string
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from govsic.constants import DORMANT, Component, SectionBoundaries
from govsic.data import SIC_GLOSSARY
from govsic.data.sections import SECTION, Section
from govsic.exceptions import InvalidSICCodeError
from govsic.parser import compute_resolutions, parse
from govsic.types import SICCode


@dataclass
class SIC:
    """
    The govsic-provided Standard Industrial Classification object to represent
    SIC instances following the current UK SIC 2007 methodology.

    Attributes:
        code (int, str): uksic07-supported code.
        level (int, None): integer depth (2-5) to truncate the sic code.
    """

    code: SICCode
    level: Optional[int] = None

    __resolutions: List[str] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        """
        Auto parse the given SIC code, check its structural validity, and compute all resolutions.
        """
        self.code = parse(self.code)

        self.__resolutions = compute_resolutions(self.code)

        if self.level is not None:
            self.set_level(self.level)

        if not 1000 <= int(self.code) <= 99999:
            raise InvalidSICCodeError(
                message="SIC is supported from Section A (01000) through Section U (99999)."
            )

    def set_level(self, level: int) -> None:
        """
        Setter method for specifying the SIC code level.

        Args:
            level (int): integer depth to set the SIC code.
        """
        if not 2 <= level <= 5:
            raise ValueError("SIC digit levels must be between 2 and 5 inclusive.")

        self.level = level
        self.code = self.__resolutions[level - 2]

    @property
    def is_valid(self) -> bool:
        """
        Check if the given SIC code is valid by official summary lookup.
        """
        return self.code in SIC_GLOSSARY

    @property
    def component(self) -> str:
        """
        Retrieve the component name for the most significant digit, e.g. 08110
        has resolution 4 and returns 'CLASS'.
        """
        relevance = str(self.code)[:-4:-1]
        for index, character in enumerate(relevance):
            if int(character) > 0:
                return list(Component)[len(str(self.code)) - index - 1].name
        return "DIVISION"

    @property
    def section(self) -> str:
        """
        Retrieve the SIC Section that the given code corresponds to.
        """
        if int(self.code) == DORMANT:
            return "DORMANT"

        bounds = [int(b.value) for b in SectionBoundaries] + [DORMANT]
        bucket = next(x[0] for x in enumerate(bounds) if x[1] > int(self.code))
        return string.ascii_uppercase[bucket - 1]

    @property
    def description(self) -> List[str]:
        """
        Retrieve the SIC description at the current level.
        """
        if self.component == "DIVISION":
            section: Section = SECTION.__dict__[self.section]
            return [section.long_description.strip()]

        return SIC_GLOSSARY[str(self.code)]


    def summary(self) -> str:
        """
        Get all relevant information about the provided SIC code, including section, code value,
        component, and description.
        """
        section: Section = SECTION.__dict__[self.section]

        if not self.is_valid:
            raise ValueError

        return " ".join([
            f"{self!r} ::",
            "\n".join([
                section.description.upper(),
                f"{[c.name for c in Component].index(self.component) + 1}-digit description:",
                *set(self.description if self.description else ""),
            ])
        ])

    def as_dict(self) -> Dict[str, Any]:
        """
        Get the dictionary respresentation of the SIC data structure with the provided code.
        """
        return {
            "value": self.code,
            "valid": self.is_valid,
            "section": self.section,
            "component": self.component,
            "description": [*set(self.description)]
        }

    def __repr__(self) -> str:
        """
        String representation of the given code, using the UK SIC 2007 format
        constructor.
        """
        div, grp_cls, sub_cls = [str(self.code)[i:i+2] for i in range(0, len(str(self.code)), 2)]
        return (
            f"[{self.section}] "
            f"{div}.{grp_cls}/{sub_cls}"
        )

    def __str__(self) -> str:
        """
        String representation of the given code.
        """
        return str(self.code)
