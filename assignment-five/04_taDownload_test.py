import pytest
from other_code.taDL import downloadSubmission

def test_taDownloadSuccess():
    download = downloadSubmission()
    assert download[0] == "CS4320"
    assert download[1] == "Assignment Five"
    assert download[2] == "William"
    assert download[3] == "fileName.py"

def test_taDownloadFailure():
    download = downloadSubmission()
    assert download[0] == "CS3050"
    assert download[1] == "Assignment Five"
    assert download[2] == "William"
    assert download[3] == "fileName.py"
