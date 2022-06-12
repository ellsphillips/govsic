from dataclasses import dataclass
from typing import Union

SICCode = Union[str, int]

@dataclass
class SIC:

    code: SICCode = ""

    def __post_init__(self) -> None:
        if len(str(self.code)) > 5:
            raise ValueError

        self.code = str(self.code).zfill(5)

    @property
    def is_valid(self) -> bool:
        return True
