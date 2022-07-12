# type: ignore

import random
import string

import pandas as pd
from govsic import SIC


def generate_id(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_uppercase, k=length))

def main() -> None:
    data = pd.DataFrame({
        "id": [generate_id() for _ in range(3)],
        "classification": ["46491", "56302", "98200"]
    })

    data["classification"] = data["classification"].map(SIC)
    data["section"] = data["classification"].map(lambda sic: sic.section)

    example: SIC = data["classification"].values[0]

    print(
        data.head(),
        example.summary(),
        sep="\n\n"
    )


if __name__ == "__main__":
    main()
