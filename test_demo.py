import pytest
def test_firstProgram():
    print("Hello hhCgyjg hinmaya")


@pytest.mark.usefixtures("browser")
def test_browser(browser):
    print(browser)