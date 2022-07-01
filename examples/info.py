# type: ignore

import json

from govsic import SIC


def main() -> None:
    example = SIC(56302)

    print(
        print(json.dumps(example.as_dict(), indent=4))
    )


if __name__ == "__main__":
    main()
