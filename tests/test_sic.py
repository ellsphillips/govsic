from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from govsic import SIC
from govsic.constants import DORMANT
from govsic.exceptions import InvalidSICCodeError
from govsic.types import Component


def test_post_init_parser() -> None:
    sic = SIC(1000)
    assert sic.code == "01000"

def test_invalid_length() -> None:
    with pytest.raises(InvalidSICCodeError) as exc_info:
        sic = SIC(123456)
        print(sic.code)

    exception_raised = exc_info.value
    assert str(exception_raised) == (
        "SIC is supported from Section A (01000) through Section U (99999)."
    )

def test_below_section_a() -> None:
    with pytest.raises(InvalidSICCodeError) as exc_info:
        sic = SIC("00123")
        print(sic.code)

    exception_raised = exc_info.value
    assert str(exception_raised) == (
        "SIC is supported from Section A (01000) through Section U (99999)."
    )

def test_class_str() -> None:
    sic = SIC(58290)
    assert str(sic) == "58290"

def test_class_repr() -> None:
    sic = SIC(58290)
    assert f"{sic!r}" == "[J] 58.29/0"

@pytest.mark.parametrize(
    "example_input, expectation",
    [
        (1300, does_not_raise()),
        (9000, does_not_raise()),
        (26514, does_not_raise()),
        (199999, pytest.raises(InvalidSICCodeError)),
    ],
)
def test_code_validity(example_input: int, expectation: Any) -> None:
    with expectation:
        assert SIC(example_input).is_valid is True

@pytest.mark.parametrize(
    "example_input, expectation",
    [
        ("05000", Component.DIVISION),
        ("05100", Component.GROUP),
        ("08110", Component.CLASS),
        ("05101", Component.SUBCLASS),
    ],
)
def test_sic_component(example_input: str, expectation: Component) -> None:
    assert SIC(example_input).component == expectation.name

@pytest.mark.parametrize(
    "example_input, expectation",
    [
        ("71121", "M"),
        ("08110", "B"),
        ("01450", "A"),
    ],
)
def test_section(example_input: str, expectation: str) -> None:
    sic = SIC(example_input)
    assert sic.section == expectation

def test_section_dormant() -> None:
    sic = SIC(DORMANT)
    assert sic.section == "DORMANT"

def test_provided_level() -> None:
    sic = SIC("1234", level=3)
    assert sic.code == "12300"

def test_level_setter() -> None:
    sic = SIC("1234")
    sic.set_level(2)
    assert sic.code == "12000"

def test_level_out_of_range() -> None:
    with pytest.raises(ValueError) as exc_info:
        sic = SIC(26514, level=6)
        print(sic.code)

    exception_raised = exc_info.value
    assert str(exception_raised) == (
        "SIC digit levels must be between 2 and 5 inclusive."
    )

def test_dictionary_container() -> None:
    expectation = {
        'value': '56302',
        'valid': True,
        'section': 'I',
        'component': 'SUBCLASS',
        'description': ['Public houses and bars']
    }

    assert SIC(56302).as_dict() == expectation
