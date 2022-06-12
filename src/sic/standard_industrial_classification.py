from dataclasses import dataclass
from typing import Union

from sic.constants import Component
from sic.data.glossary import SIC_GLOSSARY
from sic.exceptions import InvalidSICCodeError

SICCode = Union[str, int]

@dataclass
class SIC:

    code: SICCode = ""

    def __post_init__(self) -> None:
        if len(str(self.code)) > 5:
            raise InvalidSICCodeError(
                message="SIC codes should be at most 5 digits long."
            )

        self.code = str(self.code).zfill(5)

    @property
    def is_valid(self) -> bool:
        return self.code in SIC_GLOSSARY

    @property
    def component(self) -> str:
        for index, character in enumerate(str(self.code)[::-1]):
            if int(character) > 0:
                return list(Component)[len(str(self.code)) - index - 1].name
        return "DIVISION"
