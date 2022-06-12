import pytest
from sic import SIC
from sic.exceptions import InvalidSICCodeError


def test_post_init_parser():
    sic = SIC(100)
    assert sic.code == "00100"

def test_invalid_exception():
    with pytest.raises(InvalidSICCodeError) as exc_info:
        sic = SIC(123456)
        print(sic.code)

    exception_raised = exc_info.value
    assert str(exception_raised) == "SIC codes should be at most 5 digits long."
