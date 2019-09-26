import pytest
from other_code.login import login

def test_loginSuccess():
    loginAttempt = login()
    assert loginAttempt[0] == "Zach"
    assert loginAttempt[1] == "abc123"  

def test_loginFailure():
    loginAttempt = login()
    assert loginAttempt[0] == "Zack"
    assert loginAttempt[1] == "abc123"