import pytest
from govsic import SIC
from govsic.sic import SICCode


@pytest.mark.parametrize(
    "example_input, expectation",
    [
        (1300, "01300"),
        ("123", "12300"),
    ],
)
def test_type_parsing_strategies(example_input: SICCode, expectation: str) -> None:
    sic = SIC(example_input)
    assert sic.code == expectation

def test_unsupported_types() -> None:
    with pytest.raises(TypeError) as exc_info:
        sic = SIC(10.0) # type: ignore
        print(sic.code)

    exception_raised = exc_info.value
    assert str(exception_raised) == (
        "SIC codes must be provided as either str or int."
    )
