from dataclasses import dataclass
from typing import Dict, Optional, Protocol, Type, Union

from govsic.types import SICCode


@dataclass
class ParsingStrategy(Protocol):

    code: SICCode
    level: Optional[int] = None

    @property
    def result(self) -> str: ...


@dataclass
class IntegerSICParsingStrategy:

    code: SICCode
    level: Optional[int] = None

    @property
    def result(self) -> str:
        return str(self.code).zfill(5)

@dataclass
class StringSICParsingStrategy:

    code: SICCode
    level: Optional[int] = None

    @property
    def result(self) -> str:
        return str(self.code).ljust(5, "0")



PARSERS: Dict[Union[Type[int], Type[str]], Type[ParsingStrategy]] = {
    int: IntegerSICParsingStrategy,
    str: StringSICParsingStrategy
}


def parse(
    code: SICCode,
    level: Optional[int] = None,
) -> str:
    for _t, _p in PARSERS.items():
        if isinstance(code, _t):
            return _p(str(code), level=level).result
    raise TypeError("SIC codes must be provided as either str or int.")
