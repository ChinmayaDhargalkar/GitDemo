import pytest

@pytest.mark.usefixtures("testDataLoad")

class Test_fixi:
    def test_profile(self, testDataLoad):
        print(testDataLoad)
