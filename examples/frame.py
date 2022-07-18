import random
import string
from typing import Callable, Dict

import govsic
import pandas as pd

TMapping = Dict[str, Callable[[govsic.SIC], str]]


def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=length))


DATA = pd.DataFrame({
    "id": [generate_id() for _ in range(3)],
    "sic": ["95210", "56302", "10832"]
})


def main() -> None:
    DATA["sic"] = DATA["sic"].map(govsic.SIC)  # type: ignore

    mapping: TMapping = {
        "description": lambda sic: sic.description[0],
        "2-digit": lambda sic: str(sic.code)[:2],
        "section": lambda sic: sic.section,
        "section description": lambda sic: govsic.SECTIONS[sic.section].description,
    }

    for column, function in mapping.items():
        DATA[column] = DATA["sic"].map(function)  # type: ignore

    print(DATA.head())


if __name__ == "__main__":
    main()
