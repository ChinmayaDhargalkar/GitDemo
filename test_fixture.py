import pytest

@pytest.mark.usefixtures("first", "third")

class Testfix():

    def test_demo1(self):
        print("I'm test 1")

    def test_demo2(self):
        print("I'm test 2")

    def test_demo3(self):
        print("I'm test 3")

    def test_demo4(self):
        print("I'm test 4")

    def test_demo5(self):
        print("I'm test 5")
