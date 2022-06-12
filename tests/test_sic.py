import pytest
from sic import SIC


def test_post_init_parser():
    sic = SIC(100)
    assert sic.code == "00100"

def test_invalid_exception():
    with pytest.raises(ValueError):
        sic = SIC(123456)
        print(sic.code)
