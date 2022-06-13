import string
from dataclasses import dataclass
from typing import Union

from govsic.constants import Component, SectionBoundaries
from govsic.data.glossary import SIC_GLOSSARY
from govsic.exceptions import InvalidSICCodeError

SICCode = Union[str, int]

@dataclass
class SIC:

    code: SICCode = ""

    def __post_init__(self) -> None:
        if len(str(self.code)) > 5:
            raise InvalidSICCodeError(
                message="SIC codes should be at most 5 digits long."
            )

        if int(self.code) < 1000:
            raise InvalidSICCodeError(
                message="SIC is supported from Section A (01000) through Section U."
            )

        self.code = str(self.code).zfill(5)

    @property
    def is_valid(self) -> bool:
        return self.code in SIC_GLOSSARY

    @property
    def component(self) -> str:
        relevance = str(self.code)[:-4:-1]
        for index, character in enumerate(relevance):
            if int(character) > 0:
                return list(Component)[len(str(self.code)) - index - 1].name
        return "DIVISION"

    @property
    def section(self) -> str:
        bounds = [int(b.value) for b in SectionBoundaries]
        bucket = next(x[0] for x in enumerate(bounds) if x[1] > int(self.code))
        return string.ascii_uppercase[bucket - 1]

    def __repr__(self) -> str:
        div, grp_cls, sub_cls = [str(self.code)[i:i+2] for i in range(0, len(str(self.code)), 2)]
        return (
            f"[{self.section}] "
            f"{div}.{grp_cls}/{sub_cls}"
        )