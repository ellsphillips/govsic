from contextlib import nullcontext as does_not_raise
from typing import Any

import pytest
from govsic import SIC
from govsic.constants import Component
from govsic.exceptions import InvalidSICCodeError


def test_post_init_parser():
    sic = SIC(100)
    assert sic.code == "00100"

def test_invalid_exception():
    with pytest.raises(InvalidSICCodeError) as exc_info:
        sic = SIC(123456)
        print(sic.code)

    exception_raised = exc_info.value
    assert str(exception_raised) == "SIC codes should be at most 5 digits long."

def test_class_repr():
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
def test_code_validity(example_input: int, expectation: Any):
    with expectation:
        assert SIC(example_input).is_valid is True

@pytest.mark.parametrize(
    "example_input, expectation",
    [
        ("00000", Component.DIVISION),
        ("05000", Component.DIVISION),
        ("05100", Component.GROUP),
        ("08110", Component.CLASS),
        ("05101", Component.SUBCLASS),
    ],
)
def test_sic_component(example_input: str, expectation: Component):
    assert SIC(example_input).component == expectation.name

@pytest.mark.parametrize(
    "example_input, expectation",
    [
        ("71121", "M"),
        ("08110", "B"),
        ("01450", "A"),
    ],
)
def test_section(example_input: str, expectation: str):
    sic = SIC(example_input)
    assert sic.section == expectation
