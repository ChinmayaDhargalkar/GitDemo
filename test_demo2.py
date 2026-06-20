import pytest
def test_program():
    mess="hello"
    assert "he" in mess
@pytest.mark.xfail
def test_sec():
    a=20
    b=60
    assert a+b == 800, "No match"