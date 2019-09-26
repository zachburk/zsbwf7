import pytest
from other_code.studentSub import submit

def test_studentSubmitSuccess():
    sub = submit()
    assert sub[0] == "CS4320"
    assert sub[1] == "Assignment Five"
    assert sub[2] == "fileName.py"

def test_studentSubmitFailure():
    sub = submit()
    assert sub[0] == "CS4320"
    assert sub[1] == "Assignment Four"
    assert sub[2] == "fileName.py"