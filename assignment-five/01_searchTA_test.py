import pytest
from other_code.searchTA import searchTA

def test_searchTA(student_fixture):
    check = 0
    for i in range(len(student_fixture)):
        if searchTA() == student_fixture[i]:
            check = 1
    if check == 0: 
        assert False

@pytest.fixture
def student_fixture():
    students = ["Zach", "Carl", "William"]
    return students