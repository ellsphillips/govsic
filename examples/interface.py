from govsic import SIC


def main() -> None:
    sic = SIC(8110)

    print(f"{sic = }")

    for label, prop in (
        ("Code value", sic.code),
        ("Is valid?", sic.is_valid),
        ("Section", sic.section),
        ("Component", sic.component),
        ("Description", sic.description),
    ):
        print(f"{label}:\t{prop}")

    print(sic.summary())


if __name__ == "__main__":
    main()
