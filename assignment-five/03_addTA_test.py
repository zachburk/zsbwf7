import pytest
from other_code.addTA import newTA

def test_addTASuccess():
    ta = newTA()
    assert ta[0] == "Hunter"
    assert ta[1] == 123123

def test_addTAFailure():
    ta = newTA()
    assert ta[0] == "Hunter"
    assert ta[1] == 123456