import pytest
from genral import square

def test_square():
    a=3
    res = square(a)
    assert res == 9

